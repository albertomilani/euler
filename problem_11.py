#!/usr/bin/python

def trova():

  f = open ( 'grid.dat' , 'r')
  mat = [ map(int,line.split()) for line in f ]

  MAX = 0

  # sommo sulle righe  
  for i in range(0, len(mat)-3):
    for j in range(0, len(mat)):
      prod = 1
      for m in range(0,4):
        prod *= mat[i+m][j]
      if prod > MAX:
        MAX = prod

  # sommo sulle colonne
  for i in range(0, len(mat)):
    for j in range(0, len(mat)-3):
      prod = 1
      for m in range(0,4):
        prod *= mat[i][j+m]
      if prod > MAX:
        MAX = prod

  # sommo sulle diagonali "verso destra"
  for i in range(0, len(mat)-3):
    for j in range(0, len(mat[i])-3):
      prod = 1
      for m in range(0,4):
        prod *= mat[i+m][j+m]
      if prod > MAX:
        MAX = prod

  # sommo sulle diagonali "verso sinistra"
  for i in range(3, len(mat)):
    for j in range(0, len(mat[i])-3):
      prod = 1
      for m in range(0,4):
        prod *= mat[i-m][j+m]
      if prod > MAX:
        MAX = prod

  return MAX


print trova()



