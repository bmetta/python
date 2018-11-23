#!/usr/bin/python

def main():
  l = []
  for i in range(1, 101):
    if i%15 == 0:
      l.append('fuzzbuzz')
    elif i%3 == 0:
      l.append('fuzz')
    elif i%5 == 0:
      l.append('buzz')
    else:
      l.append(str(i))

  print ','.join(l)

if __name__ == '__main__':
  main()
