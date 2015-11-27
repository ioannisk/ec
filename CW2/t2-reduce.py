#!/usr/bin/python

import sys
import math

prev_key = ""

# number of documents in the corpus
D = 17.0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    # n is the |d e D : t e d|
    key, n, info = line.split("\t")
    if prev_key != key:
        if info=="NOT_IN_D1":
            print key+", d1.txt = 0"
        else:
            tf = int(info.split()[1])
            idf = math.log10( D/(1 +int(n)))
            tf_idf = tf*idf
            print key+", d1.txt ="+ str(tf_idf)
    prev_key = key

