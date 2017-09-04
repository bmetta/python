#!/usr/bin/python3.4
import random
import os
import time
import sys

def printGrid(grid, R, C, i):
  print('Iteration %d' %(i))
  print('', end=' ')
  for c in range(C):
    print('%d' %(c%10), end=' ')
  print()
  print('--'*C, end=' \n')
  for r in range(R):
    for c in range(C):
      ch = ' '
      if grid[r][c] == 1: ch = '*'
      if c == 0: print('|', end='')
      if c == (C - 1): print (ch, end='|')
      else: print (ch, end=' ')
    print()
  print('--'*C, end=' \n')

def createGrid(grid, R, C):
  for r in range(R):
    rows = []
    for c in range(C):
      rows += [0]
    grid += [rows]
  return grid

def initGrid(grid, R, C, count):
  for c in range(count):
    r = random.randint(0, R-1)
    c = random.randint(0, C-1)
    grid[r][c] = 1

def checkGridIndex(grid, r, c, R, C):
  count = 0
  for i in range(r-1, r+2):
    for j in range(c-1, c+2):
      if i >= 0 and i < R and j >= 0 and j < C:
        if not (i == r and j == c):
          count += grid[i][j]

#  print ('[%d,%d]:%d' %(r, c, count), end='\n')
  if grid[r][c] == 1:
    if count == 2 or count == 3: return 1
  else:
    if count == 3: return 1
  return 0

def updateGrid(grid, nextGrid, R, C):
  for r in range(R):
    for c in range(C):
      nextGrid[r][c] = checkGridIndex(grid, r, c, R, C)
#  return grid

def playGameOfLife(grid, nextGrid):
  i = 0
  while True:
    os.system('clear')
    i += 1
    printGrid(grid, ROWS, COLS, i)
    updateGrid(grid, nextGrid, ROWS, COLS)
    grid, nextGrid = nextGrid, grid
    time.sleep(0.2)

def readFile(grid, nextGrid, filename):
  print(filename)
  f = open(filename, 'rU')

  row = 0
  for line in f:
    line = line.strip()
    line = line.split(',')
    for i, val in enumerate(line):
      grid[row][i] = int(val)
      nextGrid[row][i] = int(val)
    row += 1

ROWS = 11
COLS = 39
def main():
  grid = []
  nextGrid = []
  createGrid(grid, ROWS, COLS)
  createGrid(nextGrid, ROWS, COLS)
  if len(sys.argv) > 1:
    readFile(grid, nextGrid, sys.argv[1])
    printGrid(grid, ROWS, COLS, 0)
  else:
    initGrid(grid, ROWS, COLS, int((ROWS*COLS)/4))
    initGrid(nextGrid, ROWS, COLS, int((ROWS*COLS)/4))
  playGameOfLife(grid, nextGrid)

if __name__ == '__main__':
  main()
