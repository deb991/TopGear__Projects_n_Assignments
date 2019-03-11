#!/usr/bin/env python -i
import os
import string
import sys
import random
import threading as t

print('This program will process 5 files at a time Max')

for x in range(1, 5):

    file__IO = input('\nEnter file name here to analize with path:: ')

    if os.path.isfile(file__IO):
        print(
            '\nFile exists & initial checking has been completed, So proceeding for the next analizing~~~ :: Flag :: 1')
        print('\nBegining initial operation for the content of that file~~~ :: Flag :: 2')

        with open(file__IO, 'r') as f:
            data = f.read( )
            line = data.splitlines( )
            words = data.split( )
            spaces = data.split(" ")
            charc = (len(data) - len(spaces))

            print('\n Line number ::', len(line), '\n Words number ::', len(words), '\n Spaces ::', len(spaces),
                  '\n Charecters ::', (len(data) - len(spaces)))

        print('EOF')


##To be followed up only command line argument & threading issue for tis program. 
