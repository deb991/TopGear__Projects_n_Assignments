#!/usr/bin/env python
import os
import sys
import numpy

##Defining Super classes here, in the first stanza.
##Later child class will be added.

class addition():                      ##One of parent class.
    def __init__(self):
        print('__add__ is being overloaded with __addMatrix__ ')


    def _add_(self):
        #__col = int(input('Enter Column value :: '))
        #__row = int(input('\nEnter Row value :: '))
        print('Remember half of the elements would be indicated with a semicolon :: ')

        mat1 = numpy.matrix(input('Enter first matrix elements **2x2 :: \n'))
        mat2 = numpy.matrix(input('Enter second matrix elements **2x2 :: \n'))

        print('First Matrics formation is : \n', mat1)
        print('\nSecond Matrics formation is : \n', mat2)

        matrix__add = numpy.add(mat1, mat2)

        print('\nAddition of 2 matrixes :: \n' ,matrix__add)


class substruction():
    def __init__(self):
        print('~~~~~~~~~~String is being compared through this parent class.~~~~~~~~~~~~')


    def subs(self):
        strn1 = input('Enter the first string :: ')
        strn2 = input('Enter the second string :: ')


        compare_str = len(strn1) - len(strn2)

        if compare_str == 0:
            print('Both string has same length :: \n', {len(strn1), strn1}, '\n', {len(strn2), strn2})
            pass

        else:
            print('Both string are different by its length ::\n', {len(strn1), strn1}, '\n', {len(strn2), strn2})
            pass

class Circle():
    def __init__(self):
        print('~~~~Through this parent class, we will calculate ~~~~')
        self.Pi = 3.14159
        self.radius =(int(input('Enter the value of radius of the circle :: ')))

    def area(self):
        area = self.Pi * (self.radius * self.radius)

        print('The Area of a circle is :: ', area)

    def circumference(self):
        circumference = (2 * self.Pi * self.radius)

        print('\nThe circumference of a circle :: ', circumference )

class circl_non_param():
    def __init__(self):
        print('This is a non-parameterize consructor & radius will be predefined.')
        self.Pi = 3.14159
        self.radius = 7

    def __area__(self):
        area = self.Pi * (self.radius * self.radius)
        print('\nThe Area of a circle is :: ', area)

    def __circumference__(self):
        circumference = (2 * self.Pi * self.radius)
        print('\nThe circumference of a circle :: ', circumference)


if __name__ == '__main__':
    mat = addition()
    sub = substruction()
    #circle = Circle()
    param_circle = circl_non_param()

    #mat._add_()
    #sub.subs()
    #circle.area()
    #circle.circumference()
    param_circle.__area__()
    param_circle.__circumference__()
