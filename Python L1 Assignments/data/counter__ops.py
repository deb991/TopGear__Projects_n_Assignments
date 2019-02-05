#!/usr/bin/env python
import os
import sys


counter = 1
def dolots(count):
  global counter
  for i in (1, 2, 3):
    counter = count + i

print(counter)
print(dolots(4))
