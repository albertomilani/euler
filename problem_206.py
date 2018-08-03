#!/usr/bin/python

#1_2_3_4_5_6_7_8_9_0

import math
from decimal import *

def trova ():

  template = ['1','2','3','4','5','6','7','8','9','0']

  n = 99999999
  while n > 0:

    nstr = list('{:08d}0'.format(n))
    result = [None]*(len(template)+len(nstr))
    result[::2] = template
    result[1::2] = nstr
    s = Decimal(long(''.join(result)))
    m = s % Decimal(3)
    if m == 0 or m == 1:
      sr = s.sqrt()
      if (sr - sr.to_integral_exact(rounding=ROUND_FLOOR)) == 0.0:
        return s, sr
    
    n -= 1

  return False

print trova()


