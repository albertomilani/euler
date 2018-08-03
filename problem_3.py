#!/usr/bin/python

import math

N=600851475143

i=4
while i < N/2+1:
  if N % i == 0:
    MAX = i
    print MAX
  i += 1

print ''
print MAX

