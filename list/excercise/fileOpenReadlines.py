#!/usr/bin/python

import sys

f = open(sys.argv[1], 'rU')

#text = f.read()
#print text

#lines = f.readlines()
#print lines
for line in f:
  print line
