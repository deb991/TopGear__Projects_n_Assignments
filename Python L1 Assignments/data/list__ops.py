#!/usr/bin/env python
import os
import sys

mylist = list(range(4))
seclist = mylist
print(seclist)

mylist.append(4) ##Append 5th Value into the existing list.
print(seclist)


seclist = mylist[:]
print(seclist)


mylist.append(5) ##Appending 6th Value into the existing List mylist.
print(seclist)


