#!/usr/bin/python

def main():
  words = raw_input('Enter: ').split()
  freq = {}
  for word in words:
      freq[word] = freq.get(word, 0) + 1
  
  words = sorted(freq.keys())
  for w in words:
    print "%s:%d" % (w, freq[w])

if __name__ == '__main__':
  main()
