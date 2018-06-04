#!/usr/bin/python

rows = 3
cols = 4

multiList = [[0 for j in range(cols)] for i in range(rows)]

for i in range(rows):
  for j in range(cols):
    print multiList[i][j],
  print
