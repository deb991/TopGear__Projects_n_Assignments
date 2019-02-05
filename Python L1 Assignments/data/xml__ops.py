#!/usr/bin/env python
import os
from xml.dom import minidom
import xml.etree.ElementTree as ET

xmlData = minidom.parse("D:\\My__Env\\PycharmProjects\\TG__lib\\Python_L1_Assignments__clone1\\data\\data.xml")
itemlist = xmlData.getElementsByTagName('item')

tree = ET.parse("D:\\My__Env\\PycharmProjects\\TG__lib\\Python_L1_Assignments__clone1\\data\\data.xml")
root = tree.getroot()

print('\n all attributes are :: ')
for elem in itemlist:
    for subelem in elem:
        print(subelem.attrib)

for elem in root:
    for subelem in elem:
        print(subelem.text)



