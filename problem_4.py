#!/usr/bin/python

def is_palindrome (n):
  return str(n) == str(n)[::-1]

def find ():

  palindromes = []
  for a in reversed(range(100,1000)):
    for b in reversed(range(100,1000)):
      prod = a*b
      print a,b,prod
      if is_palindrome(prod):
        palindromes.append(prod)

  return palindromes

pals = find()

print max(pals)


