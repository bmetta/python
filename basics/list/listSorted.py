#!/usr/bin/python2.7 -tt

a = [3, 1, 5, 10, 8]
print sorted(a)
print sorted(a, reverse=True)
print

b = ['acc', 'aaa', 'd', 'bb']
def compare(s):
  tup = []
  tup += str(len(s))
  tup.extend(s)
#  print tup
  return tuple(tup)
print sorted(b, key=len)
print sorted(b, key=compare)
#print sorted(b)
#print sorted(b, key=lambda x: len(x))
#print

#c = ['cccy', 'aaaz', 'dx', 'bbt']
#def Last(s): return s[-1]
#print sorted(c, key=Last) #sort based on last char in each string
