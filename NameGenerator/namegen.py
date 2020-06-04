#!/usr/bin/env python3

import fileinput
import random

puncs =  '.,?!:;-*"_()[]{}<>/1234567890—“”’‘–' # you may need to add more
spaces = ' ' * len(puncs)

first  = {}
follow = {}
triple = {}
for rawline in fileinput.input():

	# convert to lowercase
	lower = rawline.lower()
	
	# convert punctuation to spaces
	table = lower.maketrans(puncs, spaces)
	line = lower.translate(table)

	min_word = 2
	
	# start work here
	for word in line.split():
		if len(word) < min_word: continue
		
		#first letter
		fl = word[0]
		if fl not in first: 
			first[fl] = 1
		else: 
			first[fl] += 1
		
		#letters follow letters
		for i in range(1, len(word)):
			prev = word[i-1] 
			current = word[i] 
			if prev not in follow: 
				follow[prev] = {}
			if current not in follow[prev]: follow[prev][current] = 1
			else:						   follow[prev][current] += 1
			
		for i in range(1, len(word)):
			trip = word[i-2]
			prev = word[i-1] 
			current = word[i] 
			if trip not in triple:
				triple[trip] = {}
			if prev not in triple[trip]: 
				triple[trip][prev] = {}
			if current not in triple[trip][prev]:
				triple[trip][prev][current] = 1
			else:
				triple[trip][prev][current] += 1
		


#Create random letter		
def random_output(dict):
	rseq1 = []
	for c in dict:
		for i in range(dict[c]): 
			rseq1.append(c)		
	return rseq1[random.randint(0,len(rseq1)-1)]

#create names	
def create_name(l):
	lang = []
	#choose first letter
	lang.append(random_output(first))
	#choose following letters
	for i in range(l-1):
		lang.append(random_output(follow[lang[i]]))
	string = ''.join(lang)
	return string.capitalize()
	
for i in range(100):
	print(create_name(random.randint(2,8)))
	
	
"""
for key1 in triple:
	for key2 in triple[key1]:
		for key3 in triple[key1][key2]:
			print(key1, key2, key3, triple[key1][key2])
"""