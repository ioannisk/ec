#!/usr/bin/python

import sys

prev_line = ""

for line in sys.stdin:          # For ever line in the input from stdin
    if prev_line != line:
        print line.strip()
        prev_line = line
