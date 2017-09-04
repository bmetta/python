#!/usr/bin/python

import random

rps_map = {'r': 0, 'p': 1, 's': 2}

def play_RockPaperScissor():
  #user input
  user_choice = raw_input('Enter [r][p][s]: ')
  while user_choice not in rps_map:
    print 'wrong choice'
    user_choice = raw_input('Enter [r][p][s]: ')

  #Programer input
  my_choice = random.randint(0,2)

  #decision making
  winner = True
  
  print '[user/program]: %d/%d' % (rps_map[user_choice], my_choice)
  if rps_map[user_choice] == my_choice:
    print 'Tie'
  elif (rps_map[user_choice] - my_choice) == -2 or (rps_map[user_choice] - my_choice) == 1:
    print 'YOU WON! congratulations...'
  else:
    print 'YOU LOST :('

def main():
  play = True
  while play:
    play_RockPaperScissor()
    play = ('yes' == raw_input('\nWanna play again? Enter [yes/no]: '))

if __name__ == '__main__':
  main()
