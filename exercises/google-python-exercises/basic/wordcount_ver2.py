#!/usr/bin/python
import sys

def readFile(filename):
  f = open(filename, 'rU')
  text = f.read()
  f.close()
  words = text.strip().split()

  for word in words:
    if not word.isalpha():
      words.remove(word)
  
  return words

def getWordCountMap(words):
  word_dict = {}
  for word in words:
    if not word in word_dict:
      word_dict[word] = 1
    else:
      word_dict[word] += 1

  return word_dict

def printWords(word_map):
  sorted_words = sorted(word_map.items(), key=lambda x: x[0].lower())
  for item in sorted_words:
    print item[0], item[1]

def printTop(word_map):
  sorted_count = sorted(word_map.items(), key=lambda x: x[1], reverse=True)
  for item in sorted_count:
    print item[0], item[1]

def main():
  if len(sys.argv) != 3:
    print 'Usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  list_words = readFile(sys.argv[2])
  map_word_count = getWordCountMap(list_words)
  
  if sys.argv[1] == '--count':
    printWords(map_word_count)
  elif sys.argv[1] == '--topcount':
    printTop(map_word_count)
  else:
    print 'Invalid input'

if __name__ == '__main__':
  main()
