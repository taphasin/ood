mylist = []
quelist = []


myinput = input("Enter Input : ")
que,action = myinput.split("/")
for i in que.split(","):
    a,b = i.split(" ")
    a = int(a)
    b = int(b)
    quelist.append([a,b])

for i in action.split(","):
    if i == "D":
        if mylist == []:
            print("Empty")
        else:
            print(mylist[0])
            mylist.pop(0)
    else:
        a,b = i.split(" ")
        a = str(a)
        b = int(b)
        if a == "E":
            
            for j in quelist:
                if b == j[1]:
                    c = j[0]
            if mylist == []:
                mylist.append(b)
                
            else:
                n = len(mylist)-1
                for k in range(0,len(mylist)):
                    
                    for j in quelist:
                        if mylist[n] == j[1]:
                            l = j[0]
                    if l == c:
                        mylist.insert(n+1,b)
                        break
                    n -= 1
                if l != c:
                    mylist.append(b)