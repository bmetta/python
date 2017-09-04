#!/usr/bin/python
import re

match = re.search(r'[\w.]+@[\w.]+', 'blah nick.p@gmail.com blah blah')
if match:
  print 'match.groups()', match.groups()
  print 'match.group() ', match.group()
  print 'match.group(0)', match.group(0)
else:
  print 'Not found'

print '--------------------------'

match = re.search(r'([\w.]+)@([\w.]+)', 'blah nick.p@gmail.com blah blah')
if match:
  print 'match.groups()', match.groups()
  print 'match.group() ', match.group()
  print 'match.group(0)', match.group(0)
  print 'match.group(1)', match.group(1)
  print 'match.group(2)', match.group(2)
else:
  print 'Not found'
