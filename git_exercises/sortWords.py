#!/usr/bin/python

def main():
  word_list = raw_input('Enter words: ').strip().split(',')
  word_list = sorted(word_list)
  print ','.join(word_list)

if __name__ == '__main__':
  main()
