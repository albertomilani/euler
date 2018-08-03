#!/usr/bin/python

from sympy import *
from sympy.geometry import *


with open('p102_triangles.txt') as f:
  points = f.readlines()

origin = Point(0,0)
count = 0
for ntuples in points:
  c = ntuples.strip().split(',')
  x = Point(c[0], c[1])
  y = Point(c[2], c[3])
  z = Point(c[4], c[5])

  t = Polygon(x,y,z)

  if t.encloses_point(origin):
    count += 1

print count

