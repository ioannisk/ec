#!/usr/bin/python

import sys
import os
import re

# parse line in words.
def parse(text):
        return re.compile('\w+').findall(text)

for line in sys.stdin:                  # input from standard input
    # store token count within line
    # to reduce calculations for combiner and reducer
    token_dic  = {}

    # find from which file we are reading
    file_name = os.environ["mapreduce_map_input_file"]
    # format string such that we dont print the whole file path
    file_name = file_name.split('/')[-1:]

    line = line.strip()                 # remove whitespaces
    tokens = parse(line)               # split the line into tokens

    for token in tokens:                # write the results to standard output
        if token in token_dic:
            token_dic[token] += 1
        else:
            token_dic[token] = 1

    for key in token_dic:
        # key is the word, token_dic[key] frequency of word
        print("{0}\t{1}\t{2}".format(key, token_dic[key], file_name))

