#!/usr/bin/python
import random

def binarySearch(a, k):
  if not a:
    return False
  m = len(a)/2
  return a[m] == k or \
         binarySearch(a[:m], k) or \
         binarySearch(a[m+1:], k)

def main():
  while True:
    a = [random.randint(1, 100) for i in xrange(10)]
    a = list(set(a))
    a = sorted(a)
    print len(a)
    print a
    key = raw_input('Enter key: ')
    if key == 'exit':
      break
    print binarySearch(a, int(key))

if __name__ == '__main__':
  main()
