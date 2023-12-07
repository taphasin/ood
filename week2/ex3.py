print("*** Mod Position ***")
x , y = input("Enter Input : ").split(',')
l = []
count = 1
for i in x:
    if count % int(y) == 0:
        l.append(i)
    count += 1

print(l)