filename = "intday.txt"
file = open(filename)
lines2 = file.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
file.close() # lines2: リスト。要素は1行の文字列データ

file_id=[]
day=[]
commit_times=[]

counter = 0
for line in lines2:
    split = line.split(" \t")
    if counter == 0:
        counter += 1
        for splited in split :
            file_id.append(splited)
    else :
        day_counter = 0
        for splited in split :
            if day_counter == 0 :
                day.append(splited)
                day_counter += 1
            else :


    hashcode.append(str[0])
    day.append(str[1])
    author.append(str[2])
    #print(str[0])

filename_counter=[]

for i in range(len(hashcode)-1):

    commit_file_name = hashcode[i] + ".txt"
    commit_file = open(commit_file_name)
    commit_file_lines = commit_file.readlines()
    commit_file.close()

    for line in commit_file_lines :
        line = line.rstrip('\n')
        print(hashcode[i], end = ",")
        print(day[i], end = ",")
        print(author[i], end = ",")
        print(line, end = ",")
        print(" ", end = ",")
        if line not in filename_counter:
            filename_counter.append(line)
            print(filename_counter.index(line))
        elif line in filename_counter:
            print(filename_counter.index(line))
