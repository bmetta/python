#!/usr/bin/python
import re
#match = re.match(r'^[-+]?\d*.\d+$', '+4.50')
#match = re.match(r'^[-+]?\d*.\d+$', '-1.0')
#match = re.match(r'^[-+]?\d*.\d+$', '.5')
#match = re.match(r'^[-+]?\d*.\d+$', '-.7')
#match = re.match(r'^[-+]?\d*.\d+$', '+.7')
match = re.match(r'^[-+]?\d*.\d+$', '-+4.7')
#match = re.match(r'^[-+]?\d*.\d+$', '12.')
if match:
  print match.group()
