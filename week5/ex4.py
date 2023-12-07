class DoublyLinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.previous = None

    def __init__(self):
        self.header = self.Node("head")
        self.trailer = self.Node("tail")
        self.cursor = self.Node("|")
        self.header.next = self.cursor
        self.trailer.previous = self.cursor
        self.cursor.previous = self.header
        self.cursor.next = self.trailer
        self.size = 0

    def I_ser(self,para):
        t = self.cursor
        new = self.Node(para)
        a = t.previous
        t.previous.next = new
        new.previous = a
        new.next = t
        t.previous = new

    def B_ser(self):
        t = self.cursor
        if t.previous == self.header:
            return
        h = t.previous.previous
        h.next = t
        t.previous = h
        
    def D_ser(self):
        t = self.cursor
        if t.next == self.trailer:
            return
        b = t.next.next
        b.previous = t
        t.next = b

    def R_ser(self):
        t = self.cursor
        if t.next == self.trailer:
            return
        h = t.previous
        a = t.next
        b = t.next.next

        b.previous = t
        h.next = a
        a.previous = h
        a.next = t
        t.previous = a
        t.next = b

    def L_ser(self):
        t = self.cursor
        if t.previous == self.header:
            return
        b = t.next
        a = t.previous
        h = t.previous.previous

        h.next = t
        b.previous = a
        a.next = b
        a.previous = t
        t.next = a
        t.previous = h

x = input("Enter Input : ").split(",")

linlis = DoublyLinkedList()

for i in x:
    if i[0] == "I":
        linlis.I_ser(i[2:])
    elif i[0] == "L":
        linlis.L_ser()
    elif i[0] == "R":
        linlis.R_ser()
    elif i[0] == "B":
        linlis.B_ser()
    elif i[0] == "D":
        linlis.D_ser()

t = linlis.header.next
while t.next != None:
    print(t.data,end=" ")
    t= t.next