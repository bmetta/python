#!/usr/bin/python

import sys

def Cat(filename):
  try:
    f = open(filename, 'r')
    text = f.read()
    print '----', filename
    print text
  except IOError:
    print "IOError: file [%s] doesn't exists" %(filename)

def main():
  args = sys.argv[1:]
  for arg in args:
    Cat(arg)

if __name__ == '__main__':
  main()
