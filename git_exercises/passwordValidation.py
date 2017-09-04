#!/usr/bin/python
import  re

def getCorrectPasswords(passwords):
  corr_pass = []

  for p in passwords:
    if len(p) < 6 or len(p) > 12:
      continue
    if not re.search('[a-z]', p):
      continue
    if not re.search('[0-9]', p):
      continue
    if not re.search('[A-Z]', p):
      continue
    if not re.search('[$#@]', p):
      continue
    corr_pass.append(p)

  return corr_pass

def main():
  list_passwords = raw_input('Enter passwords: ').strip().split(',')
  correct_passwords = getCorrectPasswords(list_passwords)
  print ','.join(correct_passwords)

if __name__ == '__main__':
  main()
