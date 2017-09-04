#!/usr/bin/python
import sys
import re

def addToDict(sender, rec_list, dict_send_list):
  sender = sender.strip()
  rec_list = rec_list.strip().split(', ')

  for rec in rec_list:
    if not sender in dict_send_list:
      dict_send_list[sender] = [rec]
    else:
      dict_send_list[sender].append(rec)
    if not rec in dict_send_list:
      dict_send_list[rec] = []

def parseFile(filename):
  dict_send_list = {}
  f = open(filename, 'rU')
  text = f.read()
  tup = re.findall(r'(.*):(.*)', text)
  for sender, rec_list in tup:
    addToDict(sender, rec_list, dict_send_list)
  return dict_send_list

def graphTraversal(head, is_user_rec_map, send_rec_map):
  is_user_rec_map[head] = True

  for rec in send_rec_map[head]:
    if is_user_rec_map[rec] == False:
      graphTraversal(rec, is_user_rec_map, send_rec_map)
  return

def main():
  if len(sys.argv) != 2:
    print 'Usage: ./seperateTwoGroupUsers.py seperateTwoGroupUsers.txt'
    sys.exit(1)

  map_sender_rec = parseFile(sys.argv[1])
  map_user_isRec = {}
  for user in map_sender_rec:
    map_user_isRec[user] = False

  graphTraversal('Nick Fury', map_user_isRec, map_sender_rec)
  for user, flag in map_user_isRec.items():
    if not flag:
      print user

if __name__ == '__main__':
  main()
