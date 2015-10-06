
filename = "allcommit.txt"
file = open(filename)
lines2 = file.readlines()
file.close()

commit_times = []

commit_day = []

for line in lines2:
    line = line.rstrip("\n")
    split = line.split(" ")
    commit_day.append(split)
    print(split)

first_day = commit_day[0][0]
last_day = commit_day[len(commit_day)-1][0]

print(first_day)
print(last_day)

xaxis = range(int(first_day),int(last_day),1)

continuous_commit_number = []

for day in xaxis:
#    print(day)
    for commit_day_element in commit_day :
#        print(commit_day_element[0])
        if str(day) in commit_day_element[0] :
            #continuous_commit_number.append(day,commit_day_element[1])
            print("test")
            day_and_commit = []
            day_and_commit.append(day)
            day_and_commit.append(commit_day_element[1])
            continuous_commit_number.append(day_and_commit)
            print(day_and_commit)
    if str(day) not in continuous_commit_number :
        day_and_commit = []
        day_and_commit.append(day)
        day_and_commit.append(continuous_commit_number[-1][1])
        continuous_commit_number.append(day_and_commit)
        print(day_and_commit)
