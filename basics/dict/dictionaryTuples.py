#!/usr/bin/python

d = {'a':0, 'b':1, 'c':2}
t = d.items()
print t

t1 = dict(zip('abc', range(3)))
print t1
for key, val in t1.items():
  print key, val
