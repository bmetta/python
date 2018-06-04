#!/usr/bin/python

class Test:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def print_val(self):
    print self.a, self.b

  def __repr__(self):
    return "%s %s" %(self.a, self.b)

  def __str__(self):
    return "%s %s" %(self.a, self.b)

if __name__ == '__main__':
  t = Test(10, 20)
  t.print_val()
  print t   # calls __str__() or __repr__()
  print [t] # calls __repr__()
