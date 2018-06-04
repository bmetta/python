#!/usr/bin/python
import re

#str = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'
str = 'abaabaabaabaaefEAEOUOIouf'
for match in re.finditer(r'[^aeiou]{1}[aeiou]{2,}[^aeiou]{1}', str, flags = re.I):
  s = match.start()
  e = match.end()
  print s, e
  print str[s+1:e-1]
