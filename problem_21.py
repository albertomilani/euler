#!/usr/bin/python

NMAX = 10000

def calcola_divisori(N):
  divisori = []
  for n in xrange(1, N):
    if N % n == 0:
      divisori.append(n)
  return divisori



def solve():
  gia_visti = []
  for n in xrange(1, NMAX):
    somma_divisori_n = sum(calcola_divisori(n))




