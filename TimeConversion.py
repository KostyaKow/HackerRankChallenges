#!/bin/python3

import sys
import math

time_in = input().strip()

#to double digits
def to_dd(s_n):
   s = str(s_n)
   if len(s) == 1:
      return '0' + s
   return s

def to_secs(time_str):
   spec = time_str[-2:]
   time_raw = time_str[0:-2].split(':')
   (hour, min, sec) = map(lambda x: int(x), time_raw)

   if hour == 12:
      if spec == 'AM':
         hour = 0
      if spec == 'PM':
         spec = 'AM'

   if spec == 'PM':
      hour += 12

   return hour*60*60 + min*60 + sec

def sec_to_24(tsecs):
   hours = math.floor(tsecs / (60*60))
   mins = math.floor((tsecs - (hours*60*60))/60)
   secs = tsecs - (hours*60*60) - mins*60

   return '%s:%s:%s' % (to_dd(hours), to_dd(mins), to_dd(secs))

print(sec_to_24(to_secs(time_in)))

