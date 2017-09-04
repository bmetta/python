#!/usr/bin/python
import sys

def parseFile(stockFile):
  f = open(stockFile, 'r')
  stockList = []
  lines = f.readlines()
  print lines
  print
  for line in lines[1:]:
    stockList.append(tuple(line.strip().split(',')[1:]))
  return stockList
#  for line in f:
#     stockList.append(tuple(line.strip().split(',')))
#  return stockList[1:]

if __name__ == '__main__':
  if len(sys.argv) < 2 or len(sys.argv) > 3:
    print 'invalid args'
    sys.exit(1)
  listBlocks = parseFile(sys.argv[1])

  print listBlocks
  for block in listBlocks:
    print block
