#!/usr/bin/python
import random
import string
import time

possibleChars = ' ' + string.ascii_letters + string.digits + string.punctuation
def stringEvaluation(text, guess_text):
  for i in xrange(len(text)):
    if guess_text[i] != text[i]:
      guess_text[i] = random.choice(possibleChars)

def getGuessText(length):
  text = []
  for i in xrange(length):
    text += random.choice(possibleChars)
  return text

def main():
  text = raw_input('Enter the string: ').strip()
  guess_text = getGuessText(len(text))
  num_iter = 0
  while text != ''.join(guess_text):
    stringEvaluation(text, guess_text)
    print ''.join(guess_text)
    num_iter += 1
    time.sleep(0.1)
  print 'Target matched! that took %d generations' %(num_iter)

if __name__ == '__main__':
  main()
