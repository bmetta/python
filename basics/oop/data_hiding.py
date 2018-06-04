#!/usr/bin/python

# data hiding:
# In Python, variable will not be visible outside,
# if they starts with double underscore (__)

class Test:
  # hidden member of Test class
  __hiddenVariable = 0

  # member method that changes
  # __hiddenVariable
  def add(self, val):
    self.__hiddenVariable += val;
    print self.__hiddenVariable

if __name__ == '__main__':
  t = Test()
  t.add(5)
  t.add(10)

  # this line causes error
  #print t.__hiddenVariable

  # nothing in python is truly private
  # internally the names of private methods and attributes
  # are mangled and unmangled on the fly to make them seem
  # inaccessible by their given names
  print t._Test__hiddenVariable
