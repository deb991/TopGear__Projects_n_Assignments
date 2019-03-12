#!/usr/bin/env python -i
import os
import glob
import fnmatch

path = input('Enter the path to check source Code :: ')

if os.path.isdir(path):
    os.chdir(path)
    srcFile = glob.glob1(path, "*.py*")
    srcFile_count = len(srcFile)
    print('\nDirectory changed to the destination folder: \t', os.getcwd())
    print('\nListed files under search directory :: \t{} \nFile count :: \t{}'.format(srcFile, srcFile_count))
    #print('\nListed files under search directory :: \n\t', fnmatch.filter(os.listdir(path), "*.py*"))




print('EOP')
