#!/usr/bin/python

import sys

prev_bigram = ""
value_total = 0
bigram=""
top_20=[]


def check_and_add_top_20(bigram, value):
    global top_20
    if len(top_20) < 20:
        top_20.append( (bigram, value) )
        top_20 = sorted(top_20, key=lambda tup: tup[1], reverse=True)
    else:
        if value >= top_20[19][1]:
            top_20[19] = (bigram,value)
            top_20 = sorted(top_20, key=lambda tup: tup[1], reverse=True)

def output_top_20():
    global top_20
    for k in top_20:
        print("{0}\t{1}".format(k[1], k[0]))

for line in sys.stdin:         # For ever line in the input from stdin
    try:
        line = line.strip()         # Remove trailing characters
        bigram, value = line.split("\t", 1)
        value = int(value)
        # Remember that Hadoop sorts map output by key reducer takes these keys sorted
        if prev_bigram == bigram:
            value_total += value
        else:
            if prev_bigram:
                check_and_add_top_20(prev_bigram, value_total)
            value_total = value
            prev_bigram = bigram
    except:
        continue
if prev_bigram == bigram:  # Don't forget the last key/value pair
    check_and_add_top_20(prev_bigram, value_total)

output_top_20()
