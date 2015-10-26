#!/usr/bin/python

import sys

lowest_names = []
lowest_score = sys.maxint

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    tokens = line.split("\t", 1)
    if len(tokens) == 2:
        name = tokens[0]
        score = float(tokens[1])   
        if score < lowest_score:
        	del lowest_names[:]
        	lowest_score = score
        	lowest_names.append(name)
        elif score == lowest_score:
        	lowest_score.append(name)

for name in lowest_names:
	print ("{0}\t{1:.2f}".format(name, lowest_score))


