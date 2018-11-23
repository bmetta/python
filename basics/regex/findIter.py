#!/usr/bin/python
import re

str = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'
# rabcdeefgyYhFjkIoomnpOeorteeeeet
# 012345678901234567890123456789012

#str = 'abaabaabaabaaefEAEOUOIouf'
# abaabaabaabaaefEAEOUOIouf
# 01234567890123456789012345
for match in re.finditer(r'[^aeiou]{1}[aeiou]{2,}[^aeiou]{1}', str, flags = re.I):
  s = match.start()
  e = match.end()
  print s, e, str[s:e]
