#!/usr/bin/python
name = str(raw_input("Enter your name: "))
age = raw_input("how old are you: ")
while not age.isdigit() or len(age) > 3:
  print 'Ooops.... please enter again'
  age = raw_input("how old are you: ")
age = int(age)
year = 2016 + (100 - age)
print "Mr %s, you will turn age 100 by year %s" % (name, year)
