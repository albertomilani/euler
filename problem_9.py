#!/usr/bin/python

import math

def trovala ():
  c = 500
  b = c - 1

  found = False

  while not found:
    while b > 1:
      a = math.sqrt(c**2 - b**2)
      if (a+b+c) == 1000:
        return (a*b*c)
      b -= 1
    c -= 1
    b = c - 1


print trovala()

