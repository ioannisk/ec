#!/usr/bin/python

import sys

prev_key = ""
key = ""
value_total = 0


for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t", 1)
    value = int(value)
    if prev_key == key:
        value_total += value
    else:
        if prev_key:
            print ("{0}\t{1}".format(prev_key, value_total))
        value_total = value
        prev_key = key

if prev_key == key:
    print ("{0}\t{1}".format(prev_key, value_total))
