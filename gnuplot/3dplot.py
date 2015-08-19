filename = "intday.txt"
file = open(filename)
lines2 = file.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
file.close() # lines2: リスト。要素は1行の文字列データ

#       y1  y2  y3
#   x1  z11 z12 z13
#   x2  z21 z22 z23

file_id = []
day = []
commit_times = []

#   x1  y1  z11
#   x1  y2  z12
#   x1  y3  z13

counter = 0
for line in lines2:
    line = line.rstrip("\n")
    split = line.split(" \t")
    if counter == 0:
        counter += 1
        for splited in split :
            file_id.append(splited) #y axies
    else :
        day_counter = 0
        commit_time = []
        for splited in split :
            if day_counter == 0 :
                day.append(splited)
                day_counter += 1
            else :
                commit_time.append(splited)
                #print(splited)
        commit_times.append(commit_time)

d = 0
for day_array in day :
    f = 0
    for file_array in file_id :
        print(day_array, end = " ")
        print(file_array, end = " ")
        print(commit_times[d][f])
        f += 1
    print("")
    d += 1
