#!/usr/bin/python

import sys

lowest_names = []
lowest_score = sys.maxint

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    name, score = line.split("\t", 1)
    score = float(score)   
    if score < lowest_score:
    	del lowest_names[:]
    	lowest_score = score
    	lowest_names.append(name)
    elif score == lowest_score:
    	lowest_score.append(name)

for name in lowest_names:
	print ("{0}\t{1:.2f}".format(name, lowest_score))


