#!/usr/bin/python

ints = range(1,101)

square_sum = sum(ints)**2
sum_square = sum(map(lambda x: x**2, ints))

print (square_sum - sum_square)

