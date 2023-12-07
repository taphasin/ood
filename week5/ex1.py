class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head == None:
            self.head = Node(item)
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(item)

    def size(self):
        cur, cnt = self.head, 0
        while cur != None:
            cur, cnt = cur.next, cnt + 1
        return cnt

linlis = LinkedList()

x, jump = input("Input : ").split("/")
x = x.split()
if int(jump) > len(x):
    print("Over length")
    exit()

for i in x:
    linlis.append(i)


count = 0
t = linlis.head
while t != None:
    if count % int(jump) == 0:
        if t.next == None:
            nex = "-1"
        else:
            nex = t.next.value
        print(f"Now index {count} value is {t.value} next value is {nex}")
    t = t.next
    count += 1
    
    
