#!/usr/bin/python

import sys

prev_key = ""
key = ""
value_total = 0
max_value = 0
max_key = ""


for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t", 1)
    value = int(value)
    if prev_key == key:
        value_total += value
    else:
        if value_total > max_value:
            max_value = value_total
            max_key = prev_key
        value_total = value
        prev_key = key

print ("{0}\t{1}".format(max_key, max_value))
