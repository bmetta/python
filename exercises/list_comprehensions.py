#!/usr/bin/python
import random

def main():
  #a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  a = [random.randint(0, 100) for x in xrange(10)]
  print a
  b = [i for i in a if i%2 == 0]
  print b


if __name__ == '__main__':
  main()
