#!/usr/bin/python

class Person(object):
  # constructor
  def __init__(self, name):
    self.name_ = name

  def getname(self):
    return self.name_

  def isEmploye(self):
    return False

class Employee(Person):
  def isEmploye(self):
    return True

if __name__ == "__main__":
  p = Person('Person')
  print p.getname(), p.isEmploye()

  e = Employee('Employee')
  print e.getname(), e.isEmploye()
