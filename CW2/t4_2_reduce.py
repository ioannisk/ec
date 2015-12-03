#!/usr/bin/python

import sys
import re
import datetime

prev_key = ""
key = ""
value_total = 0
questions_list = []

max_key =""
max_value = 0
max_question_list =[]

def print_out():
    global max_key
    global max_question_list
    global max_value_total
    sys.stdout.write(max_key+"\t->\t")
    for i in max_question_list:
        sys.stdout.write("{0}, ".format(i))

for line in sys.stdin:
    line = line.strip()
    key, Id ,value = line.split("\t", 2)
    value = int(value)
    if prev_key == key:
        value_total += value
        questions_list.append(Id)
    else:
        if prev_key:
            if max_value <= value_total:
                max_value = value_total
                max_key = prev_key
                max_question_list = questions_list

        questions_list = []
        value_total = value
        prev_key = key
        questions_list.append(Id)

if prev_key == key:
    if max_value <= value_total:
        max_value = value_total
        max_key = prev_key
        max_question_list = questions_list
        questions_list = []

print_out()
print str(len(max_question_list))
