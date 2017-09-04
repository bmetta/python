#!/usr/bin/python
import random

def listOverlap(a, b):
  if len(b) < len(a):
    a, b = b, a
  
#  res = []
#  for item in a:
#    if item in b and not item in res:
#      res.append(item)
  res = [x for x in set(a) if x in b]
  return res

def main():
  a = [random.randint(0, 15) for r in xrange(10)]
  b = [random.randint(0, 15) for r in xrange(10)]

  res = listOverlap(a, b)
  print 'a          -> ', a
  print 'b          -> ', b
  print 'r          -> ', res

if __name__ == '__main__':
  main()
