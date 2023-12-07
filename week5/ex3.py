class Node:
    def __init__(self, value, point):
        self.data = value
        self.next = None
        self.interpoint = point

class LinkedList:
    def __init__(self):
        self.node_list = []

linlis = LinkedList()
x = input("Enter edges: ")
plant = x.replace(">",",")
plant = plant.split(",")
x = x.split(",")
frequency = {}
lis = []


for item in plant:
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1
      lis.append(item)

lis.sort()
frequency = dict(sorted(frequency.items()))

for thing in frequency:
    if frequency[thing] >= 3:
        point = True
    else:
        point = False
    t = Node(thing,point)
    linlis.node_list.append(t)

for linker in x:
    for value in linlis.node_list:
        if linker[0] == value.data:
            index_lin = int(lis.index(linker[2]))
            value.next = linlis.node_list[index_lin]

print(lis)
print(frequency)
for intersection in linlis.node_list:
    print(intersection.data,end=" ")
print("\n",end="")

for intersection in linlis.node_list:
    print(intersection.data,intersection.interpoint)
    if intersection.interpoint == True:
        print("in")
        t = intersection
        len_count = 1
        visited = []
        while t.next != None and t.next.data not in visited:
            print(t.data)
            visited.append(t.data)
            len_count += 1
            t = t.next
        print("node",intersection.data,len_count)

