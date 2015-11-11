#!/usr/bin/python

import sys

prev_word = ""
word = ""

# buffer for a single word info. Keys are the filenames that the word was found
# TODO SORT THIS BEFORE PRINTING
dic_buffer = {}

def print_buffer(word_prev):
    string  = word_prev + ":  " +str(len(dic_buffer)) + ":  { "
    # we use i to know when we print the last item of the dic
    help_list = [i for i in dic_buffer]
    help_list.sort()
    i = 0
    for key in help_list:
        i += 1
        if i == len (dic_buffer):
            string += "({0}, {1}) }}".format(key, dic_buffer[key])
        else:
            string += "({0}, {1}), ".format(key, dic_buffer[key])
    print string

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    word, value = line.split("\t", 1)

    # TODO change this to be able to support combiners
    # a combiner might give cat : 2 : {(d1.txt, 2), (d2.txt, 3)} output
    # reducer must be able to parse info about multiple files
    word_frequency, file_name = value.split("\t", 1)
    word_frequency = int(word_frequency)

    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_word == word:
        if file_name in dic_buffer:
            dic_buffer[file_name] += word_frequency
        else:
            dic_buffer[file_name] = word_frequency

    else:
        if prev_word:  # write result to stdout
            print_buffer(prev_word)
        # flush buffer
        dic_buffer.clear()
        prev_word = word
        dic_buffer[file_name] = word_frequency

if prev_word == word:  # Don't forget the last key/value pair
    print_buffer(prev_word)
