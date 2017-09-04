#!/usr/bin/python

import sys
import os

def listDir(dir):
  filenames = os.listdir(dir)
  print filenames

  for filename in filenames:
    path = os.path.join(dir, filename)
    print 'Relative path:', path
    print 'Absolute path:', os.path.abspath(path)

def main():
  listDir(sys.argv[1])

if __name__ == '__main__':
  main()
