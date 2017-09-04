#!/usr/bin/python
import sys
import re

def main():
  filename = sys.argv[1]
  f = open(filename, 'rU')
  user_id_map = {}
  #text = f.read()
  #list_tup = re.findall(r'(\w+):.:(\d+):', text)
  #user_id_map = dict(list_tup)
  
  for line in f:
    if not line.startswith('#'):
      words = line.split(':')
      user_id_map[words[0]] = words[2]
  
  for user in sorted(user_id_map):
    print "{}:{}".format(user, user_id_map[user])

if __name__ == '__main__':
  main()
