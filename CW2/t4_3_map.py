#!/usr/bin/python

import sys
import re
import xml.etree.ElementTree as ET

#re.compile('(?<=\ Id=\")\d+').findall(string_to_search) returns the Id

for line in sys.stdin:
    # if the lenght of the split is not 10 that means we have malformed input, we can ignore it
    try:
        m = ET.fromstring(line)
        post_type = m.attrib['PostTypeId']
        if post_type == '2':
            try:
                user = m.attrib['OwnerUserId']
                parent_q = m.attrib['ParentId']
                # ANSWER ID
                Id = m.attrib['Id']
                print ("{0}\t{1}\t{2}\t{3}".format(Id, post_type, parent_q, user))
            except:
                continue
        else:
            try:
                user = m.attrib['OwnerUserId']
                acc_ans = m.attrib['AcceptedAnswerId']
                # QUESTION ID
                Id = m.attrib['Id']
                print ("{0}\t{1}\t{2}\t{3}".format(acc_ans, post_type, Id, user))
            except:
                continue
    except:
        continue
