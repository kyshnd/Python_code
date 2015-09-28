
filename = "intday.txt"
file = open(filename)
lines2 = file.readlines()
file.close()

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
            file_id.append(splited) #file_id
    else :
        day_counter = 0
        commit_time = []
        for splited in split :
            if day_counter == 0 :
                day.append(splited) #append the first of lines to day array
                day_counter += 1
            else :
                commit_time.append(splited) #append  to commit number array
                #print(splited)
        commit_times.append(commit_time) #append all file commit to one line

d = 0
for day_array in day :
    f = 0
    all_commit = 0
    print(day_array, end = " ")
    for file_array in file_id :
        #print(file_array, end = " ")
        all_commit += int(commit_times[d][f])
        #print(commit_times[d][f])
        f += 1
    print(all_commit)
    d += 1
