#!/usr/bin/python

N=1000;

print sum(filter(lambda x: (x % 3 == 0 or x % 5 == 0), range(0,N)))


