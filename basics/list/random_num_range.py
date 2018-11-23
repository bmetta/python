#!/usr/bin/python
import random
range_min = 5
range_max = 10

for i in range(10):
  print range_min + random.random(1) * (range_max - range_min)
