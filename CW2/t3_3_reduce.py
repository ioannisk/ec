#!/usr/bin/python

import sys
import re
import datetime

prev_key = ""
key = ""
dates_list = []


def check_and_add_date(key, date):
    #datetime.timedelta = (days, seconds)
    global dates_list
    if len(dates_list) < 2:
        dates_list.append(date)
        dates_list.sort()
    else:
        if date >= dates_list[1]:
            dates_list[1] = date
        elif date <= dates_list[0]:
            dates_list[0] = date

def output_date(prev_key):
    global dates_list
    if len(dates_list)==1:
        print prev_key +"\t"+str(dates_list[0])
    else:
        print prev_key +"\t"+ str(dates_list[1]-dates_list[0])
    dates_list=[]


for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t", 1)
    #datetime(2006, 6, 14, 13, 0, tzinfo=gmt1)
    date = value.split()
    day = int(date[0])
    month = 8
    year = int(date[2])
    hours = int(date[3])
    minutes = int(date[4])
    seconds = int(date[5])
    d = datetime.datetime(year, month, day, hours, minutes, seconds)
    if prev_key == key:
        check_and_add_date(key, d)
    else:
        if prev_key:
            output_date(prev_key)
        prev_key = key
        check_and_add_date(key, d)

if prev_key == key:
    output_date(prev_key)



