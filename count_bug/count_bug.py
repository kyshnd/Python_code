#!/usr/bin/python
# coding: UTF-8
import os
import datetime
import time

filename = "XStream JIRA Export.html"
file = open(filename)
lines2 = file.readlines()
file.close()

counter = 0

for line in lines2:
    if "nav created" in line:
        counter += 1
        splited = line.split("datetime=\"")
        print(counter, end = ",")
        print(splited[1][:21], end = ",")
    elif "nav updated" in line:
        splited = line.split("datetime=\"")
        print(splited[1][:21])
#    str = line.split(" ")
#    for sepalated_str in str :
#        if sepalated_str == "class=\"nav created\"" :
#            print(line)
