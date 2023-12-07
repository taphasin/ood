data,search = input("Enter Input : ").split("/")
data = list(map(int,data.split()))
search = list(map(int,search.split()))


for i in search:
    greater = []
    for j in data:
        if j > i:
            greater.append(j)
    if greater != []:
        print(min(greater))
    else:
        print("No First Greater Value")
