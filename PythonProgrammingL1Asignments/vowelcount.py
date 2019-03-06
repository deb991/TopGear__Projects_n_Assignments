import os
import sys
import re

file = "C:\\Users\\DE635273\\PycharmProjects\\TOPGEAR__P1_D1\\res\\sample.txt"
vowel = set("AEIOUaeiou")

print("<<Flag Var -- 1>> -- reading contents from Sample input file. ")
Cont = open(file, "r")
words = Cont.read().split()
#print(Cont.read())


print("<<Flag Var -- 2>> -- Reading content from input file and determining Vowel. ")
#total_string = [Cont]

countV = 0
countC = 0
for C in words:
    if C in vowel:
        countV += 1
        print("%s Vowels are" %words)