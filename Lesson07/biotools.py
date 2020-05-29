#!/usr/bin/env python3

import sys
import gzip
import random
import math


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

#generate random sequences
def randseq(l, gc):
	dna = []
	for i in range(l):
		r = random.random()
		if r < gc:
			r = random.randint(0,1)
			if r == 0: dna.append('G')
			else:      dna.append('C')
		else:
			r = random.randint(0,1)
			if r == 0: dna.append('A')
			else:      dna.append('T')
	return ''.join(dna)
	
	
#KD scale
def haswhatiwant(protein, win, t):
	for i in range(len(protein) - (win-1)):
		sseq = protein[i:i+win]
		if kd(sseq) > t and 'P' not in sseq:
			return True
	return False
	
def kd(sseq):
	sum = 0
	for aa in sseq:
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
	return sum/len(sseq)

#gc frequency
def gc(seq):
	count = 0 
	for nt in seq:
		if nt == 'G' or nt == 'C':
			count += 1
	return count/len(seq)
	
	
#Make histograms
def histogram(seq):
	hist = []
	a, c, g, t = 0, 0, 0, 0
	for nt in seq:
		if   nt == 'A': a += 1
		elif nt == 'C': c += 1
		elif nt == 'G': g += 1
		elif nt == 'T': t += 1
	afreq = hist.append(a / len(seq))
	cfreq = hist.append(c / len(seq))
	gfreq = hist.append(g / len(seq))
	tfreq = hist.append(t / len(seq))
	return hist
	
#calculate entropy
def seq_entropy(win):
	h = 0
	hist = histogram(win)
	for i in range(len(hist)):
		if hist[i] > 0: 
			h -= hist[i] * math.log2(hist[i])
	return h


		
		
		
		
	
	
	
	
	
	