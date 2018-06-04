#!/usr/bin/python

import urllib
import sys

#print (sys.version)
#print (urllib.__file__)

uf = urllib.urlopen('http://google.com')
data = uf.read()
print (data)

urllib.urlretrieve('http://google.com/logos/doodles/2016/2016-doodle-fruit-games-day-15-5673550515011584-hp.gif', 'blah.gif')
