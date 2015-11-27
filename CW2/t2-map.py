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
# TODO parse in reducer, way faster because mapper has to parse everything

terms = []
f = open('terms.txt', 'r')
for line in f:
    terms.append(line)
f.close

for line in sys.stdin:
    # parse inverted list input
    # remove semantic characters so we can split
    line = line.strip()
    line = line.split()
    # we save the key so it wont get affected by the strinf parsing (key might contain :, {, etc...)
    key = line.pop(0)
    line = " ".join(line)
    # removing {, :, ect
    for k in parse_info:
        # TODO replace the letter from dic equivilant
        line = line.replace(k, "")
    line = line.strip()
    line = line.split()
    # check if key is in the terms document
    if key in terms:
        # save the number of documents that term appears
        n = line.pop(0)
        # reconstruct invertes list in a nice format so we can avoid parsing it again in the reducer
        buff = "NOT_IN_D1"
        for i in range(0,len(line),2):
            # output
            if line[i] == "d1.txt":
                buff = (line[i]+" "+line[i+1])
            print key +"\t" + n + "\t" + buff
