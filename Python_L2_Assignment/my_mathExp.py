#!/usr/bin/env python
import os
import sys
import math


class mathnew( ):
    def sqroot(self):
        usrInput = int(input("Enter the value to eval :: "))
        output = math.sqrt(usrInput)

        print(output)

    def addition_module(self):
        add = [int(x) for x in (input('Enter veriables here :: ').split( ))]
        output = sum(add)
        print(output)

    def substraction_module(self):

        usrInput1 = int(input('Enter the first value & the value must be larger then the second one:: '))
        usrInput2 = int(input('Enter the second value & this value must be smaller than First one :: '))

        if usrInput1 > usrInput2:
            output = usrInput1 - usrInput2
            print('Substracted value is ::  ', output)
            pass


        elif usrInput1 < usrInput2 or usrInput2 > usrInput1:
            output = usrInput2 - usrInput1

            print('Substracted value is in negetive : ' + '-', output)
            pass

        else:
            print('User Input is invald, Check it once or, try again !!')

    def multiplication_module(self):
        __mull = 1
        data = [int(y) for y in input('Enter Values to multiply all  :: ').split( )]

        for y in data:
            __mull *= y

        print(__mull)

    def division_module(self):

        usrInput1 = int(input('Enter the number to be devided :: '))
        usrInput2 = int(input('Enter the number to devide :: '))

        if usrInput1 > usrInput2:
            output = usrInput1 / usrInput2
            rem = usrInput1 % usrInput2

            print('Devides result is :: ', output, '\n When reminder after devision is :: ', rem)
            pass

        elif usrInput2 > usrInput1:
            output = float(usrInput1 / usrInput2)
            rem = usrInput1 % usrInput2

            print('Devides result is :: ', output, '\nWhen reminder after devision is :: ', rem)
            pass
        else:
            print('Please review your inputs :: \n', usrInput1, '\n', usrInput2)
            pass


if __name__ == '__main__':
    inst = mathnew( )
    inst.sqroot( )
    inst.addition_module( )
    inst.substraction_module( )
    inst.multiplication_module( )
    inst.division_module( )
