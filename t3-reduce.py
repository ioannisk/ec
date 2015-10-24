#!/usr/bin/python

import sys

line_total = 0
word_total = 0


for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    line, value = line.split("\t", 1)
    value = int(value)

    line_total += 1
    word_total += value
    

print("{0}\t{1}".format(line_total, word_total))