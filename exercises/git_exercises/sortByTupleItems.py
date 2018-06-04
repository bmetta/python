#!/usr/bin/python

def getInput():
  i = 1
  tup = []
  while True:
    data = raw_input('Enter record %d: ' %(i))
    if not data:
      break
    tup.append(tuple(data.split(',')))
    i += 1

  return tup
def main():
  persons_details = getInput()
  persons_details = sorted(persons_details)
  print persons_details

if __name__ == '__main__':
  main()
