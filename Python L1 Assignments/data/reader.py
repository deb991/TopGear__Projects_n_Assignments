#!/usr/bin/env python
import os
import sys
import string
from collections import Counter

input__file = r"D:\\My__Env\\PycharmProjects\\TG__lib\\Python_L1_Assignments__clone1\\data\\inout.txt"
output__file = r"D:\\My__Env\\PycharmProjects\\TG__lib\\Python_L1_Assignments__clone1\\redir\\output.txt"


with open(input__file, 'r') as reading:
    s = reading.read()
    lines = s.splitlines()
    words = s.splitlines()


    for line in lines:
        sys.stdout = open(output__file, 'a+')
        print('Charecter numbers as per Line numbers. :: ', + len(line))  ## Flag Ver #1
        sys.stdout.close()



words = Counter(input__file)        ##Counting each of the word from the source file.
sys.stdout = open(output__file, 'a+')
print('Words per Line :: ', words)  ## Flag Ver #2
sys.stdout.close()

char__count = Counter(input__file)
sys.stdout = open(output__file, 'a+')
print("Charecters count within:: ", + char__count) ##Flag ver #3
sys.stdout.close()
