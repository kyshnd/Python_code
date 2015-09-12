#!/usr/bin/python
# coding: UTF-8
import os

start_year = "1996"
start_month = "01"
monthly_files = []
months = 1
years = int(start_year)
for years in range(int(start_year),2016) :
    for months in range(1,13) :
        if months < 10 :
            jointed = str(years) + "0" + str(months)
            monthly_files.append(jointed)
            print(jointed)
        else :
            jointed = str(years)+ str(months)
            monthly_files.append(jointed)
            print(jointed)

commit_counter = 0
for monthly_file in monthly_files :
    if os.path.exists(monthly_file + ".txt") :
#        print(monthly_file + ".txt")

        filename = monthly_file + ".txt"
        file = open(filename)
        lines2 = file.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
        file.close() # lines2: リスト。要素は1行の文字列データ

        commit_counter = len(lines2)

        human_names=[]

        for line in lines2:
            str = line.split(" ")
            human_names.append(str[2])

        #count human numbers

        counted_human_names = []
        human_counter = 0

        for human_name in human_names:
            counted = human_name
            if counted not in counted_human_names:
                counted_human_names.append(counted)
                human_counter += 1

        #for counted_human_name in counted_human_names:
        #    print(counted_human_name)
        print(monthly_file + "01", end=" ")
        print(human_counter, end=" ")
        print(commit_counter)
