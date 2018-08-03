#!/usr/bin/python

primes = [2]

def is_prime(n):
  global primes
  for p in primes:
    if numero % p == 0:
      return False
  return True

somma = 2
numero = 3;
while numero < 2000001:
  
  if is_prime(numero):
    primes.append(numero)
    somma += numero
    print numero, somma

  numero += 1    
  
print somma


