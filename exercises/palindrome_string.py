#!/usr/bin/python

def palindrome(word):
  rev_word = word[::-1]
  print rev_word
  if word == rev_word:
    return True
  return False

def main():
  str = 'ABCBA'
  if palindrome(str):
    print 'palindrome', str
  else:
    print 'not palindrome', str

  str = 'ABBA'
  if palindrome(str):
    print 'palindrome', str
  else:
    print 'not palindrome', str

  str = 'ABCD'
  if palindrome(str):
    print 'palindrome', str
  else:
    print 'not palindrome', str

if __name__ == '__main__':
  main()
