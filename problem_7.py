#!/usr/bin/python

primes = [2]

def is_prime(n):
  global primes
  for p in primes:
    if numero % p == 0:
      return False
  return True


numero = 3;
while len(primes) < 10001:
  
  if is_prime(numero):
    primes.append(numero)

  numero += 1    
  
print len(primes)


