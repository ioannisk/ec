#!/usr/bin/python

import sys

prev_col = ""
value_total = 0
col = ""
trans_row = []


def output_row(row, cell_list):
    cell_list = sorted(cell_list, key=lambda tup: tup[0])
    sys.stdout.write("{0} ".format(row))
    for cell in cell_list:
        sys.stdout.write("{0} ".format(cell[1]))
    print 

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    col, value = line.split("\t", 1)
    row, cell = value.split()

    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if (prev_col != "") and (prev_col != col):
        output_row(prev_col, trans_row)
        del trans_row[:]    #flush cell list 
    trans_row.append( (int(row), cell) )
    prev_col = col
    
if prev_col == col:  # Don't forget the last key/value pair
    output_row(prev_col, trans_row)