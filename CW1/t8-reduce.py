#!/usr/bin/python

import sys

prev_key = ""
results = []

def output_row(data):
	# mark tuples have more elements than student tuples
	# we can sort the buffer based on list lenght and therefore get studetn info before grades
	data.sort(key = lambda s: len(s))
	sys.stdout.write("{0} -->".format(data[0][1]))
	for i in range(1, len(data) ) :
		sys.stdout.write(" ({0}, {1})".format(data[i][1], data[i][2]))
	print
	
for line in sys.stdin:
	line = line.strip()
	info = line.split()
	key = info[0]

	if (prev_key != "") and (prev_key != key):
		output_row(results)
		del results[:]
	results.append(info)
	prev_key = key

if prev_key == key:
	output_row(results)

