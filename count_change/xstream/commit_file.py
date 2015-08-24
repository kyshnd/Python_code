filename = "output.txt"
file = open(filename)
lines2 = file.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
file.close() # lines2: リスト。要素は1行の文字列データ

hashcode=[]
day=[]
author=[]

for line in lines2:
    str = line.split(" ")
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
