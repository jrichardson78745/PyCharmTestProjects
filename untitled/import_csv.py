#!/usr/bin/python3

import csv
with open('CISSP_Wait_Period.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print your_list
# [['This is the first line', 'Line1'],
#  ['This is the second line', 'Line2'],
#  ['This is the third line', 'Line3']]
