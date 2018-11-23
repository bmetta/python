#!/usr/bin/python
import re

match = re.search(r'[\w.]+@[\w.]+', 'blah nick.p@gmail.com blah blah')
if match:
  print 'match.groups()', match.groups()    # ()
  print 'match.group() ', match.group()     # nick.p@gmail.com
  print 'match.group(0)', match.group(0)    # nick.p@gmail.com
else:
  print 'Not found'
print '--------------------------'

match = re.search(r'([\w.]+)@([\w.]+)', 'blah nick.p@gmail.com blah blah')
if match:
  print 'match.groups()', match.groups()    # ('nick.p', 'gmail.com')
  print 'match.group() ', match.group()     # nick.p@gmail.com
  print 'match.group(0)', match.group(0)    # nick.p@gmail.com
  print 'match.group(1)', match.group(1)    # nick.p
  print 'match.group(2)', match.group(2)    # gmail.com
else:
  print 'Not found'
