#!/usr/bin/python

# reduce: continually applies the function to the sequence.
# syntax: reduce(function, iterable[, initializer])
# returns: single value

# sum of all values of a list
total = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6])
print total

total = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6], 10)
print total

# max value of a list
max_val = reduce(lambda x, y: x if x > y else y, [47, 11, 42, 102, 13])
print max_val

max_val = reduce(lambda x, y: x if x > y else y, [47, 11, 42, 102, 13], 1010)
print max_val
