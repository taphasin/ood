count = 0
def deleteIsland(Map,y,x):
    if x < 0 or y < 0:
        return

    Map[x][y] = 0

    try:
        if Map[x-1][y] == 1:
            #Map[x-1][y] = 0
            deleteIsland(Map,y,x-1)
    except:
        pass

    try:
        if Map[x+1][y] == 1:
            #Map[x+1][y] = 0
            deleteIsland(Map,y,x+1)
    except:
        pass

    try:
        if Map[x][y-1] == 1:
            #Map[x][y-1] = 0
            deleteIsland(Map,y-1,x)
    except:
        pass

    try:
        if Map[x][y+1] == 1:
            #Map[x][y+1] = 0
            deleteIsland(Map,y+1,x)
    except:
        pass
    return Map,x,y


def countIsland(Map,x = 0,y = 0):
    global count
    if len(Map[x]) == y:
        x += 1
        if len(Map) <= x:
            return count
        y = 0

    if Map[x][y] == 1:
        Map,x,y = deleteIsland(Map,y,x)
        count += 1
    y += 1
    return countIsland(Map,x,y)


Input = input("Enter Input : ").split('/')
Map=[]
for i in Input:

    temp=[*i]
    temp = list(map(int,temp))
    Map.append(temp)

print(f"Island have : {countIsland(Map)}")


