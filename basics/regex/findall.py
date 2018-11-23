#!/usr/bin/python
import re

list_strings = re.findall(r'[\w.]+@[\w.]+', 'blah nick.p@gmail.com blah blah rick.r@bar')
print list_strings
print '------------------------------------'

list_tuples = re.findall(r'([\w.]+)@([\w.]+)', 'blah nick.p@gmail.com blah blah rick.r@bar')
print list_tuples
