filename = "d:\\github\\xstream\\Analysis\\output.txt"
file = open(filename)
lines2 = file.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
file.close() # lines2: リスト。要素は1行の文字列データ

hashcode=[]

for line in lines2:
    str = line.split(" ")
    hashcode.append(str[0])
    #print(str[0])

for i in range(len(hashcode)-1):
    print("git diff --stat --name-only", end = " ")
    print(hashcode[i], end = " ")
    print(hashcode[i+1], end = " ")
    print("> " + hashcode[i] + ".txt" )
