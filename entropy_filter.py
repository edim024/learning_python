#!/usr/bin/env python3

import argparse
import biotools as bt
import random
import math

# Write a program that masks areas of low complexity sequence
# Use argparse for command line arguments (see example below)
# Use read_fasta() from biotools.py

# setup
parser = argparse.ArgumentParser(
	description='Brief description of program.')
	
# required arguments
parser.add_argument('--input', required=True, type=str,
	metavar='<path>', help='FASTA file')

# optional arguments with default parameters
parser.add_argument('--window', required=False, type=int, default=15,
	metavar='<int>', help='optional integer argument [%(default)i]')
parser.add_argument('--threshold', required=False, type=float, default=1.1,
	metavar='<float>', help='optional floating point argument [%(default)f]')
# switches
parser.add_argument('--lowercase', action='store_true',
	help='on/off switch')
	
# finalization
arg = parser.parse_args()

#seqs = ['ACGT', 'ACAC', 'ACGN', 'NNNN', 'ACGTN']
#for seq in seqs:
#	print(seq, seq_entropy(seq))




for name, seq in bt.read_fasta(arg.input):
	eseq = []
	for nt in seq:
		eseq.append(nt)
	for i in range(len(seq) - arg.window + 1):
		win = seq[i:i+arg.window]
		if bt.seq_entropy(win) < arg.threshold:
			for j in range(i, i+arg.window):
				if arg.lowercase:
					eseq[j] = eseq[j].lower()
				else: eseq[j] = 'N'
	mseq = ''.join(eseq)
	for i in range(0, len(mseq), 60):
		print(mseq[i:i+60])
	

			
#each sequence, need window to find low entropy region 
#create windows

"""


python3 entropy_filter.py --help
usage: entropy_filter.py [-h] --input <path> [--window <int>]
                         [--threshold <float>] [--lowercase]

Low complexity sequence masker.

optional arguments:
  -h, --help           show this help message and exit
  --input <path>       fasta file
  --window <int>       optional integer argument [15]
  --threshold <float>  entropy threshold [1.100000]
  --lowercase          report lower case instead of N


python3 entropy_filter.py --input genome.fa.gz | head -20
>I
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAAAAATTGAGATAAGAAAACATTTTACTTTTTCAAAATTGTTTTCATGC
TAAATTCAAAACNNNNNNNNNNNNNNNAAGCTTCTAGATATTTGGCGGGTACCTCTAATT
TTGCCTGCCTGCCAACCTATATGCTCCTGTGTTTAGGCCTAATACTAAGCCTAAGCCTAA
GCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAA
GCCTAAGACTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAA
GCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAA
GCCTAAGACTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAA
GCCTAAAAGAATATGGTAGCTACAGAAACGGTAGTACACTCTTCTGNNNNNNNNNNNNNN
NTGCAATTTTTATAGCTAGGGCACTTTTTGTCTGCCCAAATATAGGCAACCAAAAATAAT
TGCCAAGTTTTTAATGATTTGTTGCATATTGAAAAAAACANNNNNNNNNNNNNNNGAAAT
GAATATCGTAGCTACAGAAACGGTTGTGCACTCATCTGAAANNNNNNNNNNNNNNNNNNN
NNGCACTTTGTGCAGAATTCTTGATTCTTGATTCTTGCAGAAATTTGCAAGAAAATTCGC
"""
