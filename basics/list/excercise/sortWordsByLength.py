#!/usr/bin/python
import sys
import re

def readFile(filename):
  f = open(filename, 'rU')

  words = []
  for line in f:
    line = line.strip()
    if line:
      words.extend(re.split('\s*,\s*', line))
#      words = words + re.split('\s*,\s*', line) # same as above
  f.close()
  return words

def sortCompare(w):
  return (len(w), w)

def sortWords(words):
  res = []
  res = sorted(words, key=sortCompare, reverse=True)
#  res = sorted(words, key=lambda x: (len(x), x), reverse=True)# same result as above
  return res

def sortWordTuples(words):
  t = []
  for word in words:
    t.append((len(word), word))
    t = sorted(t, reverse=True)

  res = []
  for length, word in t:
    res.append(word)

  return res

if __name__ == '__main__':
  if len(sys.argv) < 2 or len(sys.argv) > 3:
    print 'Usage ./sortWordsByLength.py sortWordsByLength.txt'
    sys.exit(1)

  list_words = readFile(sys.argv[1])
  print list_words
  print

  words = sortWords(list_words) 
#  words = sortWordTuples(list_words) # same result as above method
  print words
