#!/usr/bin/python

import sys

def fibonacci(num):
  a, b = 0, 1
  fib = []
  for i in xrange(num):
    fib.append(b)
    a, b = b, a+b
  return fib

def main():
  if len(sys.argv) < 2:
    print 'usage ./fibonacci num'
    sys.exit(1)

  list_fib = fibonacci(int(sys.argv[1]))
  print list_fib

if __name__ == '__main__':
  main()
