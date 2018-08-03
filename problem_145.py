#!/usr/bin/python

def reverse(num):
  return int(str(num)[::-1])

n = 1;
count = 0
while n < 10**3:
  rn = reverse(n)
  if len(str(n)) == len(str(rn)):
    s = n + rn
    if s % 2:
      count += 1
  n += 1

print count

