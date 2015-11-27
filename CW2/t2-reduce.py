#!/usr/bin/python

import sys
import math

# number of documents in the corpus
D = 16.0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    # n is the |d e D : t e d|
    key, n, info = line.split("\t", 2)
    if info=="NOT_IN_D1":
        print key+", d1.txt = 0"
    else:
        tf = int(info.spit()[1])
        idf = math.log10( D/(1 +n) )
        tf_idf = tf*idf
        print key+", d1.txt ="+ str(tf_idf)


