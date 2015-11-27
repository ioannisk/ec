#!/usr/bin/python

import sys

prev_word = ""
word = ""

# buffer for a single word info. Keys are the filenames that the word was found
# TODO SORT THIS BEFORE PRINTING
dic_buffer = {}

def print_buffer(word_prev):
    string  = word_prev + " : " +str(len(dic_buffer)) + " : { "
    # we use i to know when we print the last item of the dic
    # this step wi
    help_list = [int(i.split(".")[0][1:]) for i in dic_buffer]
    help_list.sort()
    help_list = [("d"+str(i)+".txt") for i in help_list]
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
    word, file_info = line.split("\t", 1)
    values = file_info.split("\t")

    # reducer must be able to parse info about multiple files

    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_word == word:
        for value in values:
            file_name, word_frequency = value.split()
            word_frequency = int(word_frequency)

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
        for value in values:
            file_name, word_frequency = value.split()
            word_frequency = int(word_frequency)
            dic_buffer[file_name] = word_frequency

if prev_word == word:  # Don't forget the last key/value pair
    print_buffer(prev_word)
