#!/usr/bin/python
import random

# Get even numbers from a generated random numbers
a = [random.randint(0, 100) for x in xrange(10)]
print a
b = [i for i in a if i%2 == 0]
print b

# squares
squares = [x**2 for x in [1, 2, 3, 4, 5]]
print squares

#intersection of two lists
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
intersection = [x for x in list_a if x in list_b]
#intersection = [x for x in list_a for y in list_b if x==y]
print intersection
