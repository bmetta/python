#!/usr/bin/python

import random

def play_guessingGame():
  random_num = random.randint(1, 9)
  guess_count = 0
  guess_num = 0

  while guess_num != random_num:
    guess_count += 1
    guess_num = raw_input('Enter: ')
    if guess_num == 'exit':
      break;
    guess_num = int(guess_num)
    
    if random_num < guess_num:
      print 'too high'
    elif random_num > guess_num:
      print 'too low'
    else:
      print 'match!!! in %d tries' % (guess_count)

def main():
  play_guessingGame()

if __name__ == '__main__':
  main()
