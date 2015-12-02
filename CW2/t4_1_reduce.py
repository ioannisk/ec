#!/usr/bin/python

import sys
import re
import datetime

prev_key = ""
key = ""
top_10=[]

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
        print("{0}\t{1}").format(k[1], k[0])



for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t", 1)
    #datetime(2006, 6, 14, 13, 0, tzinfo=gmt1)
    if prev_key == key:
        pass
    else:
        if prev_key:
            check_and_add_top_10(prev_key, value)
        prev_key = key

output_top_10()



