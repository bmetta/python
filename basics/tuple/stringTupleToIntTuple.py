#!/usr/bin/python

t = ('1', '2', '3')
print (t)

t1 = tuple(int(x) for x in t)
#t1 = map(int, t)

print (t1)
