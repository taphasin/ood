x = input("Enter Input : ")
li = []
for i in x:
    li.append(i)

a = li.count("(")
b = li.count(")")
c = li.count("[")
d = li.count("]")


sum = abs((a - b)) + abs((c - d))

print(sum)
if sum == 0:
    print("Perfect ! ! !")
