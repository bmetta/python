#!/usr/bin/python
import thread
import time

list1 = [11, 12, 13, 14, 15, 16, 17, 18, 19]
list2 = [21, 22, 23, 24, 25, 26, 27, 28, 29]

def validate(lst, threadName):
  for i in lst:
    time.sleep(1)
    print (threadName, i, "\n")

def main():
  try:
    thread.start_new_thread(validate, (list1, 'thread_1'))
    thread.start_new_thread(validate, (list2, 'thread_2'))
  except:
    print ('Unable to start thread')
  
  while True:
    pass

main()
