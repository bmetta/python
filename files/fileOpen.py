#!/usr/bin/python
# sum of nth column items
import sys

print ("Here's your file %r:" % sys.argv[1])

#f = open(sys.argv[1], 'r')
with open(sys.argv[1], 'r') as f:

total = 0
for line in f:
  print (line.split(' '))
  for i, num in enumerate(line.split(' ')):
#    print (i, int(num))
    if i == 2:
      total +=  int(num)

print (total)

f.close()
