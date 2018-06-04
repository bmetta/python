#!/usr/bin/python
import threading
import time

class myThread(threading.Thread):
  def __init__(self, threadID, name, lst, delay):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name
    self.lst = lst
    self.delay = delay

  def run(self):
    print("Starting " + self.name)
    displayList(self.name, self.lst, self.delay)
    print("Exiting  " + self.name)

def displayList(threadName, lst, delay):
  print threadName
  for i in lst:
    time.sleep(delay)
    print (threadName, i)

def main():
  list1 = [0, 1, 2, 3, 4]
  list2 = [5, 6, 7, 8, 9]

  thread1 = myThread(1, 'source', list1, 1)
  thread2 = myThread(2, 'target', list2, 2)

  thread1.start()
  thread2.start()

  thread1.join()
  thread2.join()
  print ('Exiting main thread')

main()
