#!/bin/python3

import sys

time_in = input().strip()

first = time_in[0:-2]
spec = time_in[-2:]

add_hour = 0
if spec == 'PM':
    add_hour = 12


def fix_hour(h):
    add_hour = 0
    if spec == 'PM':
        add_hour = 12
    new_h = str(int(h) + add_hour)
    if len(new_h) == 1:
        new_h = '0' + new_h
    return new_h

splitted = first.split(':')
#splitted[0] = str(int(splitted[0]) + add_hour)
splitted[0] = fix_hour(splitted[0])

if time_in == '12:00:00AM':
   print('00:00:00')
elif time_in == '12:00:00PM':
    print('12:00:00')
else:
    print(':'.join(splitted))
