#!/usr/bin/env python -i
import os
import string
import sys
import random
import threading
import getopt

def cat():

    if os.path.isfile(file__IO):
        with open(file__IO, 'r') as f:
            data = f.read()
            line = data.splitlines()
            words = data.split()
            spaces = data.split(" ")
            chareters = (len(data) - len(spaces))

            print(' \nLine Number :: {}, \t Word Number :: {}, \t Spaces :: {}, \t charecters :: {}'.format(len(line), len(words), len(spaces), chareters))

thread_list = []

print('This program will process 5 files at a time Max')
for x in range(1, 6):
    file__IO = input('\tEnter file name here to analize with path:: ')

    t = threading.Thread(target=cat)
    thread_list.append(t)

#Starting threading

for thread in thread_list:
    t.daemon = True
    thread.start()


for thread in thread_list:
    thread.join()

print('\nEnd of program')

