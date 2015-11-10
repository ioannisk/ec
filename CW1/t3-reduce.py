#!/usr/bin/python

import sys

line_total = 0
word_total = 0


for line in sys.stdin:          # For ever line in the input from stdin
	try:
		line = line.strip()         # Remove trailing characters
		line, value = line.split("\t", 1)
		value = int(value)

		line_total += 1
		word_total += value
	except:
		continue

print("{0}\t{1}".format(word_total, line_total))