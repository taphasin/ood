Queue = []

def find_portal():
    error = True
    arrived = []
    combi = [(-1,0),(0,1),(1,0),(0,-1)]
    while error:
        current = Queue.pop(0)
        current = tuple(reversed(current))
        arrived.append(current)

        for loop in combi:
            xplus = int(current[0]+loop[0])
            yplus = int(current[1]+loop[1])

            if (xplus,yplus) not in arrived and (yplus,xplus) not in Queue:
                if 0 <= xplus < co and 0 <= yplus < ro:
                    z = make_map[xplus][yplus]
                    if z == "_":
                        Queue.append(tuple((yplus,xplus)))
                    elif z == "O":
                        print("Found the exit portal.")
                        error = False
                        quit()
        if len(Queue) <= 0:
            print("Cannot reach the exit portal.")
            error = False
            quit()
        print("Queue:",Queue)



def find_f():
    for i in range(len(make_map)):
        if "F" in make_map[i]:
            Queue.append(tuple((make_map[i].index("F"),i)))
            return
    
    print("Invalid map input.")
    quit()

        
            

user = input("Enter width, height, and room: ").split()
ro = int(user[0])
co = int(user[1])
make_map = user[2].split(",")

if len(make_map) != co:
    print("Invalid map input.")
    quit()

for a in make_map:
    if len(a) != ro:
        print("Invalid map input.")
        quit()

find_f()
print("Queue:",Queue)
find_portal()