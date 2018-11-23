#!/usr/bin/python

# map() : applies a given function to each item of an iterable (list,tuple etc.)
#         and returns a list of the results
# syntax: map(function, iterable, ...)
#   function -> map() passes each item of the iterable to this function
# returns a list of the results

# Convert temp from Celsius to Fahrenheit
# F = (9 / 5) * C + 32
# C = (5 / 9) * F - 32
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit  = map(lambda c : ((9/5) * c) + 32, Celsius)
print Fahrenheit

# Square
items_square = map(lambda item : item * item, [1, 2, 3, 4, 5])
print items_square

# two list multiplications
powers = map(lambda x, y : x * y, [1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
print powers
