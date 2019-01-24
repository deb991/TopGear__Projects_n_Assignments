#!/usr/bin/env python
import os
import string


def isListOfInts():
    chkList = [input("Enter the inout here to eval & check :: ")]

    for item in chkList:
        try:
            int_val = int(item)
            print( True )
            print( "\n List contents only integer type data.:: >> ", chkList)
        except item == None:
            print( "\n List contents nothing/ blank.:: >> ", chkList)
            pass
        except ValueError:
            print( 'arg not of <list> type', chkList)
            pass

if __name__ == '__main__':
    isListOfInts()

