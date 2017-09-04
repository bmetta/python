#!/usr/bin/python
import sys

def main():
  filename = sys.argv[1]
  f = open(filename, 'rU')
#  list_of_lines = f.readlines()
#  print list_of_lines[-1].strip()
  for line in f:
    pass
  print line.strip()

if __name__ == '__main__':
  main()
