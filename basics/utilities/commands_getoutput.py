#!/usr/bin/python
import sys
import os
import commands

def listDir(dir):
  (status, output) = commands.getstatusoutput('ls -l ' + dir)
  if status:
    print sys.stderr, 'there was an error: ', output
    sys.exit(1)
  print output

def infoFile(filename):
  status = commands.getstatus(filename)
  print status

def main():
  args = sys.argv[1:]
  if args[0] == '--dir':
    listDir(args[1])
  elif args[0] == '--file':
    infoFile(args[1])

if __name__ == '__main__':
  main()
