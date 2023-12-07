print("*** Election ***")
people = input("Enter a number of voter(s) : ")
vote_list = []
vote_list = input().split(" ",int(people))

for c in reversed(vote_list):
    if int(c) < 0 or int(c) > 20:
        vote_list.remove(c)

if len(vote_list) <= 0:
    print("*** No Candidate Wins ***")
    exit()

counter = {}
max_count = 0
most_common_items = []
    
for item in vote_list:
    if item in counter:
        counter[item] += 1
    else:
        counter[item] = 1
        
    if counter[item] > max_count:
        max_count = counter[item]
        most_common_items = [item]
    elif counter[item] == max_count:
        most_common_items.append(item)

most_common_items.sort(key=int)
for i in most_common_items:
    print(i,end=" ")
