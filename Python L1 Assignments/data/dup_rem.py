#!/usr/bin/env python
import os


testList = []

for i in range(0, 8):
    number = int(input('Enter the value into the List ~~:: '))
    testList.append(number)


remDup = (set(testList))
print(remDup)