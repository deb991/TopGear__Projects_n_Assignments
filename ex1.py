#!/usr/bin/env python
import os


# noinspection PyTypeChecker
def ruler():
    print("Initiating ruler function...")
    num = int(input("Enter the value to Eval::  "))

    expNumrange = 1234567890

    if num%2 == 0:
        for i in range(num):
            print(expNumrange,end='----')

    else:
        rem = num%2
        remLen = len(str(abs(rem)))
        expNumrangelen = len(str(abs(expNumrange)))
        finval = len(str(abs(expNumrange - remLen)))
        setVal = expNumrange - finval
        #rem2 = (str(expNumrange) - str(remLen))
        for i in range(num):
            print(expNumrange, end=(str(setVal) + '--'))



if __name__ == '__main__':
    ruler()