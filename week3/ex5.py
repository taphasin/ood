ls = []

def count_tree():
    highest = 0
    sum = 0
    for i in reversed(ls):
        if i > highest:
            highest = i
            sum += 1
    
    return sum

d = False
c = 0

x = input("Enter Input : ").split(",")
for i in x:
    i = i.split()
    if i[0] == "A":
        # if d == True:
        #     if int(i[1]) % 2 == 0:
        #         c = -1
        #     else:
        #         c = 2
        ls.append(int(i[1]) + c)

    elif i[0] == "B":
        print(count_tree())
    elif i[0] == "S":
        for a in range(len(ls)):
            if ls[a] % 2 == 0:
                ls[a] -= 1
            else:
                ls[a] += 2



    # elif i[0] == "S" and d == False:
    #     d = True
    #     for a in range(len(ls)):
    #         if ls[a] % 2 == 0:
    #             ls[a] -= 1
    #         else:
    #             ls[a] += 2