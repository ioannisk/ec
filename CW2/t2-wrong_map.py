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
            buff += (b[i]+" "+b[i+1]+" ")
