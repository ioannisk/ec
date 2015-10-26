#!/usr/bin/python

import sys

prev_line = ""

for line in sys.stdin:          # For ever line in the input from stdin
	line = line.strip()
    if prev_line != line:
        print line
        prev_line = line
