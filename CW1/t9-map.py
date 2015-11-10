#!/usr/bin/python

import sys
import re

for line in sys.stdin:
	line = line.strip()
	line = line.split(" ", 2)
	if len(line) == 3:
		name = line[0]
		scores = re.compile('\d+').findall(line[2])
		if len(scores) > 4:
			avg = sum([ int(s) for s in scores])/float(len(scores))
			print("{0}\t{1:.2f}".format(name, avg))