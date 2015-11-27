#!/usr/bin/python

import sys

parse_info = {
    "{": "",
    "}": "",
    ",": "",
    ":": "",
    ")": " ",
    "(": ""
}
# parse part1 output, keep only words that exist in d1.txt
# calculate tf-idf, reducer is just bin/cat and n=1


# parse part1 output, key,  |d ∈ D : t ∈ d| that is the second number, n=17
# and  f(t, d) is the number after d1.txt


# TODO parse in reducer, way faster because mapper has to parse everything

terms = []
f = open('terms.txt', 'r')
for line in f:
    terms.append(line)
f.close()

for line in sys.stdin:
    # parse inverted list input
    # remove semantic characters so we can split
    line = line.strip()
    for key in parse_info:
        line = line.replace(key, parse_info[key])
    line = line.split()
    # save key and number of documents
    key = line.pop(0)
    if key in terms:
        n = line.pop(0)
        # reconstruct invertes list in a nice format so we can avoid parsing it again in the reducer
        buff = ""
        for i in range(0,len(b),2):
            if b[i] = "d1": # or smth like that
                buff += (b[i]+" "+b[i+1]+" ")
