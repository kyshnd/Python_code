#!/usr/bin/python
# coding: UTF-8
import os
import datetime

filename = "change_history_view.csv"
file = open(filename)
lines2 = file.readlines()
file.close()

date_axis = []
module_axis = []

count_row = 0
for line in lines2:
    if count_row > 1:
        count_row += 1
        #Date,Author,File,Attribution,ID
        str = line.split(",")
        string_date = str[0]
        if int(str[4]) not in module_axis :
            module_axis.append(int(str[4]))

        tdatetime = datetime.datetime.strptime(string_date, '%Y-%m-%d')
        tdate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)

        if tdate not in date_axis :
            date_axis.append(tdate)
    else :
        count_row += 1


module_axis.sort()
date_axis.sort()

x_max = len(date_axis)
y_max = len(module_axis)

print(x_max)
print(y_max)

module_id_commit = [[0 for i in range(y_max)] for j in range(x_max)]

#print(module_id_commit)

count_row = 0
for line in lines2:
    if count_row > 1:
        count_row += 1
        #Date,Author,File,Attribution,ID
        str = line.split(",")
        commit_date = str[0]
        commit_target_id = int(str[4])

        tdatetime = datetime.datetime.strptime(commit_date, '%Y-%m-%d')
        input_commit_date = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)

        if input_commit_date in date_axis:
            x_axis = date_axis.index(input_commit_date)
            y_axis = module_axis.index(commit_target_id)

            module_id_commit[x_axis][y_axis] += 1
    else :
        count_row += 1


d=0
for module in module_id_commit:
    d += 1
    m=0
    for commit in module:
        print(date_axis[d-1], end=" ")
        print(module_axis[m], end=" ")
        print(commit)
        m += 1
    print()
