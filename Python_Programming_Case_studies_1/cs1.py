#!/usr/bin/env python
import os
import sys
from datetime import *
from subprocess import Popen

outputFileName = 'Output'
cmpltName = outputFileName + ".txt"
output__file = "D:\\My__Env\\PycharmProjects\\TG__lib\\output__data\\Output.txt"

def find__dir():
    srch__path = input('Enter directory path :: ')


    for path, subdir, files in os.walk(srch__path):
        for name in srch__path:

            thePath = os.path.join(srch__path)
            to__thePath = os.chdir(srch__path)
            theFiles = list(os.listdir(os.getcwd()))

            #for name in files:
            for something in theFiles:


                theDictc = dict()
                theStats = os.stat(something)
                theDictc[something] = theStats

                for item in theDictc:
                    with open(output__file, "a") as f:
                        print("The File: {:30s} The Size: {:d} Bytes".format(item, theDictc[item].st_size), os.path.join(path, name), file=f)

                        
                        ========================================================
                        
                        #def file__analizer():
    #file__IO = input('\nEnter file name here to analize with path:: ')
    #if os.path.isfile(file__IO):
    #    print('\nFile exists & initial checking has been completed, So proceeding for the next analizing~~~ :: Flag :: 1')

    #    print('\nBegining initial operation for the content of that file~~~ :: Flag :: 2')

    #   with open(file__IO, 'r') as f:
    #        for line in f:
    #            print(f.read())
    #            line__count = len(f.readline())
    #            print(line__count)
    #        f.close()

    #    file__dict = dict()


#if __name__ == '__main__':
#    find__dir()
