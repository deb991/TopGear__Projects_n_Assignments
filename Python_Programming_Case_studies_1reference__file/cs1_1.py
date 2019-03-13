#!/usr/bin/env python -i
import os
import sys
import threading
import getopt

def cat(argv):
    input_file = ''
    output_file = ''

    try:
        opts, args = getopt.getopt(argv, "hi:o:",["ifile=","ofile="])
    except getopt.GetoptErrora:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('Input file is "', input_file)
    print('Output file is "', output_file)

if __name__ == '__main__':
    cat(sys.argv[1:])
