#!/usr/bin/python

import sys

prev_bigram = ""
value_total = 0
bigram=""

for line in sys.stdin:          # For ever line in the input from stdin
    try:
        line = line.strip()         # Remove trailing characters
        bigram, value = line.split("\t", 1)
        value = int(value)
        # Remember that Hadoop sorts map output by key reducer takes these keys sorted
        if prev_bigram == bigram:
            value_total += value
        else:
            if prev_bigram:  # write result to stdout
                print("{0}\t{1}".format(prev_bigram, value_total))
            value_total = value
            prev_bigram = bigram
    except:
        continue

if prev_bigram == bigram:  # Don't forget the last key/value pair
    print("{0}\t{1}".format(prev_bigram, value_total))