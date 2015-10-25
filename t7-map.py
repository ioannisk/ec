#!/usr/bin/python

import sys

row = 0

for line in sys.stdin:                  # input from standard input
    line = line.strip()                 # remove whitespaces
    tokens = line.split()               # split the line into tokens
    for col in range(0,len(tokens)):                # write the results to standard output
    	# use col as the key, pass row as part of the value so reducer can sort it
        print("{0}\t{1} {2}".format(col, row, tokens[col]))
    row += 1