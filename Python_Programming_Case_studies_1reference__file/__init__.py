#!/usr/bin/env python
import os
import random

outputFileName = 'Output'
cmpltName = outputFileName + ".txt"
output__file = "C:\\Users\\DE635273\\PycharmProjects\\TG_proj\\output__data\\Output.txt"


def find__dir():
    srch__path = input('Enter directory path :: ')

    for path, subdir, files in os.walk(srch__path):
        for name in srch__path:

            thePath = os.path.join(srch__path)
            to__thePath = os.chdir(srch__path)
            theFiles = list(os.listdir(os.getcwd()))

            # for name in files:
            for something in theFiles:

                theDictc = dict()
                theStats = os.stat(something)
                theDictc[something] = theStats

                for item in theDictc:
                    with open(output__file, "a") as f:
                        print("The File: {:30s} The Size: {:d} Bytes".format(item, theDictc[item].st_size),
                              os.path.join(path, name), file=f)
