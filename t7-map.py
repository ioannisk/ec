#!/usr/bin/python

import sys


for line in sys.stdin:                  # input from standard input
    line = line.strip()                 # remove whitespaces
    row, tokens = line.split("\t", 1)               # split the line into tokens
    tokens = tokens.split()
    for col in range(0, len(tokens)):                # write the results to standard output
        # use col as the key, pass row as part of the value so reducer can sort it
        print("{0}\t{1} {2}".format(col, row, tokens[col]))
