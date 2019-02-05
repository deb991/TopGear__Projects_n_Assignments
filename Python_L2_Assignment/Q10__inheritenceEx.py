#!/usr/bin/env python
import os
import sys


class first():
    def __init__(self):
        print('This is the fist class, which will be inharited by second & third class in this program \n')
        self.order = 1

    def method1(self):
        order = self.order
        print(order)
        pass

class second(first):
    def __init__(self):
        first.__init__(self)
        self.order = 3

    def method1(self):
        order = self.order
        class_ordervar = order * 2
        print(order, '\n', class_ordervar)
        pass

class third(first):
    def __init__(self):
        first.__init__(self)
        self.order = 7

    def method1(self):
        order = self.order
        class_ordervar = order * 2
        print(order, '\n', class_ordervar)
        pass

class fourth(second, third):
    def __init__(self):
        print('~~~~Initiating fourth Class & this is a flag~~~~')
        second.__init__(self)
        third.__init__(self)
        self.order = 31

    def method1(self):
        order = self.order
        class_ordervar = order * 2
        print(order, '\n', class_ordervar)
        pass

if __name__ == '__main__':
    f1 = first()
    f2 = second()
    f3 = third()
    f4 = fourth()

    f1.method1()
    f2.method1()
    f3.method1()
    f4.method1()
