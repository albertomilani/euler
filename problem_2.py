#!/usr/bin/python

a = 1
b = 1
f = a + b
somma = 0

while f < 4000000:
  f = a + b
  if f % 2 == 0:
    somma += f
  b = a
  a = f

print somma


