#!/usr/bin/python

import sys
import re 

def find_bigrams(input_list):
	return zip(input_list, input_list[1:])

def parse(text):
	return re.compile('\w+').findall(text)

def stringify(bigram):
	return bigram[0] + " " + bigram[1]

lines_read = 0
for line in sys.stdin:
	tokens = find_bigrams(parse(line))
	if len(tokens)==2:
		for token in tokens:
			print("{0}\t{1}".format(stringify(token),1))