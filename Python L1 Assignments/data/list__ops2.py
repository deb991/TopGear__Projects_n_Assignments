#!/usr/bin/env python

list1 = [int(x) for x in input().split()]   #Directly taking inouts from User as per the expectration
list2 = [int(x) for x in input().split()]   #Directly taking inouts from User as per the expectration
list3 = [int(x) for x in input().split()]   #Directly taking inouts from User as per the expectration

print(max(list1), '\n', max(list2), '\n', max(list3))
print(min(list1), '\n', min(list2), '\n', min(list3))

maxList = [max(list1), max(list2), max(list3)]
minList = [min(list1), min(list2), min(list3)]

print(maxList, '\n', minList)