#!/usr/bin/python

import random
import string

def passwordGen1():
  all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&?@^_`'
  passcode = []
  for i in xrange(10):
    ch = random.choice(all_chars)
    passcode.append(ch)
  return passcode

def passwordGen2(size = 8, chars=string.printable):
  return ''.join(random.choice(chars) for i in range(size))

def main():
  password = passwordGen2()
  print password

if __name__ == '__main__':
  main()
