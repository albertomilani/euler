
from decimal import *

somma = Decimal(0)
f = open ( 'numbers.dat' , 'r')
for line in f:
  somma = somma + Decimal(line)

print somma

