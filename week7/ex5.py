def asteroid_collision(asts,index = 0):
    if len(asts)-1 <= index or asts == []:
        return asts

    if asts[index] >= 0 and asts[index+1] < 0:
        if abs(asts[index]) > abs(asts[index+1]):
            asts.pop(index+1)
            return asteroid_collision(asts,index-1)
        elif abs(asts[index]) < abs(asts[index+1]):
            asts.pop(index)
            return asteroid_collision(asts,index-1)
        else:
            asts.pop(index)
            asts.pop(index)
            return asteroid_collision(asts,index-2)
    return asteroid_collision(asts,index+1)


x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))