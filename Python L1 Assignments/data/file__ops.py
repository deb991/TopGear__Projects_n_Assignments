#!/usr/bin/env python
import os
import subprocess
from ctypes import windll
import string

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

print('\ninitiating File checing into current Directory >>>...\n')


def file__Manager():
    print('\ninitiating File checing into current Directory >>>...\n')
    parent_dir = ('/')
    print('\n Root filesystem syntex depends upon Platforms. ~~~~')
    print(
        '\nWindows File system starts with \n<<C as Primary Parent Drive>>\n <<"/" as Primary Parent Drive/ Directory Location for both Unix, Mac>>')
    try:
        print('Parent Directory:: ~~~~\n')
        # noinspection PyTypeChecker
        #os.system(start'C:\\Users')
        subprocess.call("explorer C:\\Users\\", shell = True)

    except:
        print('Parent Directory:: ~~~~\n')
        os.system('START "/"')


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)

        bitmask >>= 1

    print(drives)

def file_indexing():
    print('\nIndexing whole drive of the system:: >>....')
    directory = ('C:\\Users\\')
    baseDir = "D:\\My__Env\\PycharmProjects\\TG__lib"
    # try:
    #       with open('index.txt', 'a') as f:
    #           print(root, file = f)


    #except FileNotFoundError:
    #   print('[WinError 3] The system cannot find the path specified')

    thePath = os.getcwd()
    theFiles = list(os.listdir(thePath))

    theDict = dict()
    for something in theFiles:  # Calculate size for all files here.
        theStats = os.stat(something)
        theDict[something] = theStats

    for item in theDict:
        print("The File: {:30s} The Size: {:d} Bytes".format(item, theDict[item].st_size))
###Incomplete###


if __name__ == '__main__':
    file__Manager()
    get_drives()
    file_indexing()