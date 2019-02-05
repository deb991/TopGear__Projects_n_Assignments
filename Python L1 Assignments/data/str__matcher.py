#!/usr/bin/env python
import os
import sys
import string

data = input('Enter the string to test it: ')
words = data.split()


for word in words:
    for chars in word:
        print([chars])
        print(data.find('e'))
        print(word.find('e'))

print(data[3]) ## Buffer

## Need to optimised & make precise output.
