#!/usr/bin/python

import sys
import re
import xml.etree.ElementTree as ET

#re.compile('(?<=\ Id=\")\d+').findall(string_to_search) returns the Id

for line in sys.stdin:
    # if the lenght of the split is not 10 that means we have malformed input, we can ignore it
    try:
        m = ET.fromstring(line)
        # user = m.attrib['OwnerUserId']
        view_count = m.attrib['ViewCount']
        # post_type 1 for question 2 for answer
        post_type = m.attrib['PostTypeId']
        Id = m.attrib['Id']
        if post_type=='1':
            print('{0}\t{1}'.format(Id,view_count))
    except:
        continue
