#!/usr/bin/python

import sys

lines_read=0
for line in sys.stdin:
	line =line.strip()	
	tokens = line.split()
	print("{0}\t{1}".format(line,len(tokens)))