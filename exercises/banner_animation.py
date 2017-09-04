#!/usr/bin/python
#----------------------------------------------
# Animated Banner Program
# More programs at UsingPython.com/programs
#----------------------------------------------
#----------------------------------------------------------------
# Challenges:
#
# 1. Change the display width to 5. Note what happens.
# 2. Add more letters to the characters dictionary.
# 3. Make a banner for your name, or a chosen message.
# 4. Allow the user to enter their message.
# 5. Print a border around the edge of the display.
# 6. Allow the user to choose their banner character [*/#/etc.].
#    (HINT: to do this, turn the dictionary into a binary image).
#----------------------------------------------------------------
#allows us to clear the console screen.
import os
import time
#the width of the display
#(the windows console is 79 characters wide).
WIDTH = 79
CHAR_LEN = 5
SPACE_LEN = 2
#the message we wish to print
message = "hello!".upper()
#the printed banner version of the message
#this is a 7-line display, stored as 7 strings
#initially, these are empty.
printedMessage = [ "","","","","","","" ]

#a dictionary mapping letters to their 7-line
#banner display equivalents. each letter in the dictionary
#maps to 7 strings, one for each line of the display.
characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " " ],

               "E" : [ "*****",
                       "*    ",
                       "*    ",
                       "*****",
                       "*    ",
                       "*    ",
                       "*****" ],
               
               "H" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *",
                       "*   *" ], 

               "O" : [ "*****",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*****" ],

               "L" : [ "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*****" ],

               "!" : [ "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "     ",
                       "  *  " ]
               }

#build up the printed banner. to do this, the 1st row of the
#display is created for each character in the message, followed by
#the second line, etc..

BANNER_ROWS = len(characters[" "]) #7

for row in range(BANNER_ROWS):
  for char in message:
    printedMessage[row] += (str(characters[char][row]) + "  ")

#the offset is how far to the right we want to print the message.
#initially, we want to print the message just off the display.
offset = WIDTH
while True:
  os.system("clear")
  #print each line of the message, including the offset.
  word_start = max(0, offset*-1)
  word_end   = WIDTH - offset
  border_start = 0
  border_end   = max(0, (WIDTH - offset - (CHAR_LEN + SPACE_LEN)*len(message)))
  print "-" * (WIDTH + 4)
  for row in range(BANNER_ROWS):
    print(" " * border_start + "|"),
    print(" " * offset + printedMessage[row][word_start:word_end]),
    print(" " * border_end + "|")
  print "-" * (WIDTH + 4)
  #move the message a little to the left.
  offset -=1
  #if the entire message has moved 'through' the display then
  #start again from the right hand side.
  if offset <= ((CHAR_LEN + SPACE_LEN)*len(message)) * -1:
      offset = WIDTH
  #take out or change this line to speed up / slow down the display
  time.sleep(0.1)
