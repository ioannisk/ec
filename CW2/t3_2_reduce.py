#!/usr/bin/python

import sys

prev_key = ""
key = ""
value_total = 0
top_10 = []

def check_and_add_top_10(key, value):
    global top_10
    if len(top_10) < 10:
        top_10.append((key, value))
        top_10 = sorted(top_10, key=lambda tup: tup[1], reverse=True)
    else:
        if value >= top_10[9][1]:
            top_10[9] = (key, value)
            top_10 = sorted(top_10, key=lambda tup: tup[1], reverse=True)

def output_top_10():
    global top_10
    for k in top_10:
        print("{0}\t{1}").format(k[0], k[1])


for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t", 1)
    value = int(value)
    if prev_key == key:
        value_total += value
    else:
        if prev_key:
            check_and_add_top_10(prev_key, value_total)
        value_total = value
        prev_key = key

if prev_key == key:
    check_and_add_top_10(prev_key, value_total)

output_top_10()
