import os

class FOO():
  def __init__(self):
    pass

  def set_something(self, value):
    self.values = value

  def do_something(self, x, y):
    #os.system("clear")
    z = self.values[x] * self.values[y]
    print "%r * %r = %r" % (self.values[x], self.values[y], z)
  
  
class BAR():
  def __init__(self, f):
    self.foo1 = f
  
  def something_else(self, a, b):
    self.foo1.do_something(a, b)

foo = FOO()
foo.set_something([1, 2, 3, 4, 5])
bar = BAR(foo)
bar.something_else(1, 2)
