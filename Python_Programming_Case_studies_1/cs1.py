#!/usr/bin/env python
import os
import string
import sys
import random
import threading as t

file__IO = input('\nEnter file name here to analize with path:: ')

if os.path.isfile(file__IO):
    print(
        '\nFile exists & initial checking has been completed, So proceeding for the next analizing~~~ :: Flag :: 1')
    print('\nBegining initial operation for the content of that file~~~ :: Flag :: 2')

    with open(file__IO, 'r') as f:
        print(f.readline(), 'Flag :: 3')
        lineCount = len(f.readlines())
        data = f.read()

        for word in data.split():
            print('Count__Word ::', len(word), 'Flag :: 4')


    print('\nTotal number of lines :: ', lineCount, 'Flag :: 5')
    f.close()
