#!/usr/bin/python

import sys

prev_col = ""
value_total = 0
col = ""
trans_row = []

def output_row(cell_list):
	cell_list = sorted(cell_list, key=lambda tup: tup[0])
	for cell in cell_list:
		sys.stdout.write("{0} ".format(cell[1]))
	print 

for line in sys.stdin:
	line = line.strip()
	col, value = line.split("\t", 1)
	row, cell = value.split()

	if prev_col == col:
		trans_row.append( (int(row), cell) )
		prev_col = col 
	else if prev_col != "":
		#row is complete, flush it
		output_row(trans_row)
		del trans_row[:]	#flush cell list 
		prev_col = col
		trans_row.append( (int(row), cell) )

	if prev_col == "":
		trans_row.append( (int(row), cell) )
		prev_col = col 