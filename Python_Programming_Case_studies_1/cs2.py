#!/usr/bin/env python -i
import os
import glob
import re

path = input('Enter the path to check source Code :: ')

if os.path.isdir(path):
    os.chdir(path)
    srcFile = glob.glob1(path, "*.py*")
    srcFile_count = len(srcFile)
    print('\nDirectory changed to the destination folder: \t', os.getcwd())
    print('\nListed files under search directory :: \t{} \nFile count :: \t{}'.format(srcFile, srcFile_count))
    #print('\nListed files under search directory :: \n\t', fnmatch.filter(os.listdir(path), "*.py*"))

    for root, dir, files in os.walk(path):
        for name in srcFile:
            print('++++++++++++\tBegining Sequesce\t++++++++++++++++\n')
            print(name)
            with open (name, 'r') as f:
                data = f.read()
                #print(data)
                lines = data.splitlines()
                print('line_count =\t',  len(lines))

                pat = re.compile(r"class+[^:]*")
                for line in lines:
                    print('Class found from entier Py scripts ::-- \t{}\n'.format((re.search(pat, data).group())))
                    print('++++++++++++\tEnd Of sequence\t++++++++++++++++\n')
                    break


else:
    print('\nPlease try again with same directory :: ')

print('EOP')
