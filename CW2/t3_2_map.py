#!/usr/bin/python

import sys


for line in sys.stdin:
    line = line.strip()
    line = line.split()
    # if the lenght of the split is not 10 that means we have malformed input, we can ignore it
    if len(line) == 10:
        # we parse the input
        host = line[0]
        timestamp = line[3] + line[4]
        # req_method+req_dir+req_http concatenated are the whole request
        req_method = line[5]
        req_web_server  = line[6]
        req_http = line[7]
        reply = line[8]
        bytes = line[9]
        print('{0}\t{1}'.format(req_web_server, 1))
