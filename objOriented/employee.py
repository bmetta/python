#!/usr/bin/python
class Employee:
  'Common base class for all employees'
  empCount = 0

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1
  
  def displayCount(self):
    print "total Employees: %d" % Employee.empCount

  def displayEmployee(self):
    print "Name: %s, Salary: %d" %(self.name, self.salary)


if __name__ == '__main__':
  emp1 = Employee("Zara", 1000)
  emp2 = Employee("Lara", 2000)

  print "total Employees: %d" % Employee.empCount
  emp1.displayEmployee()
  emp2.displayEmployee()

  print "Employee.__doc__   : ", Employee.__doc__
  print "Employee.__name__  : ", Employee.__name__
  print "Employee.__module__: ", Employee.__module__
  print "Employee.__bases__ : ", Employee.__bases__
  print "Employee.__dict__  : ", Employee.__dict__
