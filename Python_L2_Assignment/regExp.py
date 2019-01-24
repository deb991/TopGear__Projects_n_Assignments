#!/usr/bin/env python
import os
import sys
import re
import regex


class regExp():
    def __init__(self):
        print('~~~~~~Initiating regrualr expression program to extract data from given string~~~~')

    def regu(self):
        data = input('Enter the string to be evaluted. :: ')

        mail_ids = re.findall(r'[\w.-]+@', data)
        mail_domain = re.findall(r'@[\w.-]+', data)
        timeStamp = re.findall(r'\d{2}:\d{2}:\d{2}', data)
        year = re.findall(r'\d{4}', data)
        #month = re.findall(r'')


        print(mail_ids, '\n', mail_domain, '\n', timeStamp, '\n', year)


if __name__ == '__main__':
    inst = regExp()
    inst.regu()