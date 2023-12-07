que = []

def order(found):
    for o in reversed(range(len(que))):
        #print(o,",",que[o][0],",",found[0])
        #print(que)
        if que[o][0] == found[0]:
            que.insert(o+1,found)
            return
    que.append(found)

def check(f,s):
    for i in s:
        if i[0] == 'E':
            for found in f:
                if i[2:] in found:
                    if len(que) > 0:
                        order(found)
                    else:
                        que.append(found)
        elif i[0] == 'D':
            if len(que) > 0:
                print(que.pop(0)[2:])
            else:
                print("Empty")



pre_que, y =input("Enter Input : ").split("/")

pre_que = pre_que.split(",")
y = y.split(",")


check(pre_que,y)

