#!/usr/bin/env python
import os
import re


# noinspection PyTypeChecker
def isWhiteLine():
    str = input("Please enter the string for check:: ")

    if str.__contains__(' ') and str.__contains__('\t'):
        # noinspection PyTypeChecker
        print(True)
        print('\n String contents both White Space & Tab charecter.:: >>  ', str.split())
    elif str.__contains__(' ') or str.__contains__('\t'):
        print('\n String content either White space or, Tab charecter.:: >>', str.split())
    else:
        print('String does not content space or, Tab charecter.:: >>', str.split())

if __name__ == '__main__':
    isWhiteLine()
