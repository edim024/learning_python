#!/usr/bin/env python3

import gzip
import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

def read_fasta(filename):
	name = None
	seqs = []
	
	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()


def haswhatiwant(protein, win, t):
	for i in range(len(protein) - (win-1)):
		sseq = protein[i:i+win]
		if kd(sseq) > t and 'P' not in sseq:
			return True
	return False
	
def kd(sseq):
	sum = 0
	for aa in seq:
		if   aa == 'I': sum += 4.5
		elif aa == 'V': sum += 4.2
		elif aa == 'L': sum += 3.8
		elif aa == 'F': sum += 2.8
		elif aa == 'C': sum += 2.5
		elif aa == 'M': sum += 1.9
		elif aa == 'A': sum += 1.8
		elif aa == 'G': sum += -0.4
		elif aa == 'T': sum += -0.7
		elif aa == 'S': sum += -0.8
		elif aa == 'W': sum += -0.9
		elif aa == 'Y': sum += -1.3
		elif aa == 'P': sum += -1.6
		elif aa == 'H': sum += -3.2
		elif aa == 'E': sum += -3.5
		elif aa == 'Q': sum += -3.5
		elif aa == 'D': sum += -3.5
		elif aa == 'N': sum += -3.5
		elif aa == 'K': sum += -3.9
		else:			sum += -4.5
	return sum/len(seq)
	

for name, seq in read_fasta('proteins.fasta.gz'):
	n_term = seq[0:30]
	c_term = seq[30:len(seq)]
	if haswhatiwant(n_term, 8, 2.5) and haswhatiwant(c_term, 11, 2.0):
		print(name)



"""
A signal peptide is indicated by aa of > 2.5
    I, V, L, F 
in the first 30 aa

Hydrophobic region is indicated by aa > 2.0
    I, V, L, F, C
in the last 30 aa

No P!

python3 transmembrane.py proteins.fasta.gz
18w
Dtg
Krn
Lac
Mcr
PRY
Pxt
Pzl
QC
Ror
S1P
S2P
Spt
apn
bai
bdl
bou
bug
cue
drd
ft
grk
knk
ksh
m
nac
ort
rk
smo
thw
tsg
waw
zye
"""
