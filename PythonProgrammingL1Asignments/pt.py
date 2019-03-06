#!/usr/bin/env python
import os
import sys
import math

pasO = int(input("Enter the value for Pascle evaluate :: "))

def pascle_formation(pasO):
    print('Initializing Pascle pyramid conversion .. ')

    for line in range(0, pasO):                 #declearing initial range & then following for next row.
        for i in range(0, line + 1):            #After inital declearation, we are following top the next row with line range + 1
            print(binomialCoeff(line, i),
                  " ", end = "")

        print()

def binomialCoeff(pasO, k):                     #Here we are defining Binomial function.
    res = 1
    if (k > pasO - k):
        k = pasO - k
    for i in range(0, k):
        res = res * (pasO - i)
        res = res // (i + 1)

    return res
print(pascle_formation(pasO))


if __name__ == '__main__':
    pascle_formation