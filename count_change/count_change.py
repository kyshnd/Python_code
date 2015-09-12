filename = "d:\\github\\xstream\\Analysis\\output.txt"
file = open(filename)
lines2 = file.readlines() # read by 1 line to the end
file.close() # lines2 is an array

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
