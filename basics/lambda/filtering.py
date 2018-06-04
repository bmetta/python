#!/usr/bin/python

# filtering: creates a list of elements for which a function returns true
# syntax: filter(function_object, iterable)

# Even numbers

even_items = filter(lambda x : x % 2 == 0, [1, 2, 3, 4, 5, 6])
print even_items

odd_items = filter(lambda x : x % 2, [1, 2, 3, 4, 5, 6])
print odd_items


# intersection of two lists
a = [1, 2, 3, 5, 7, 9]
b = [2, 3, 5, 6, 7, 8]
intersection = filter(lambda x: x in a, b)
print intersection
