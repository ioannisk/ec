#!/usr/bin/python

import sys

for line in sys.stdin:
	line = line.strip()
	tokens = line.split()
	if tokens[0] == "student":
		#case student
		#token[1] is stid
		#token[2] is name
		print("{0}\t{1}".format(tokens[1], tokens[2]))
	elif tokens[0] == "mark":
		#case mark
		#token[1] is course name
		#token[2] is stid
		#token[3] is course mark 
		print("{0}\t{1} {2}".format(tokens[2], tokens[1], tokens[3]))