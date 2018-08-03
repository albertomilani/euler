#!/usr/bin/python

def collatz (n):
  count = 1
  while n > 1:
    if n % 2 == 0:
      n = n / 2
    else:
      n = 3 * n + 1
    count += 1
  return count

max_c = 0
max_n = 0

n = 1000000
while n > 1:
  c = collatz(n)
  if c > max_c:
    max_c = c
    max_n = n
  print n, c, max_n, max_c
  n -= 1

print max_n, max_c

