class DoublyLinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.previous = None

    def __init__(self):
        self.header = self.Node("head")
        self.trailer = self.Node("tail")
        self.header.next = self.trailer
        self.trailer.previous = self.header
        self.size = 0

    def __str__(self):
        self.straight = ""
        t = self.header
        while t.next != self.trailer:
            t = t.next
            self.straight = self.straight + t.data + "->"
        return self.straight[:-2]

    def str_reverse(self):
        self.reverse = ""
        t = self.header
        while t.next != self.trailer:
            t = t.next
            self.reverse = t.data + "->" + self.reverse
        return self.reverse[:-2]


    def append(self, data):
        p = self.Node(data)
        p.next = self.trailer
        p.previous = self.trailer.previous
        p.previous.next = p
        p.next.previous = p
        self.size += 1
        
    def addbefore(self,data):
        p = self.Node(data)
        p.previous = self.header
        p.next = self.header.next
        p.previous.next = p
        p.next.previous = p
        self.size += 1

    def insert(self,raw):
        index,data = raw.split(":")
        if int(index) < 0 or int(index) > self.size:
            print("Data cannot be added")
            return 
        print(f"index = {index} and data = {data}")
        p = self.Node(data)
        t = self.header
        for i in range(int(index)+1):
            t = t.next
        p.previous = t.previous
        p.next = t
        t.previous.next = p
        t.previous = p
        self.size += 1

    def remove(self,find):
        t = self.header
        index = -1
        while t.next != None:
            if t.data == find:
                front = t.previous
                back = t.next
                t.previous.next = back
                t.next.previous = front
                print(f"removed : {find} from index : {index}")
                self.size -= 1
                return
            t = t.next
            index += 1
        print("Not Found!")
        return

    def is_empty(self):
        return self._size == 0
    
    def process(self, x):
        self.straight = []
        self.reverse = []
        raw = x
        for i in raw:

            for j in i:
                if j == " ":
                    i = i[1:]
                else:
                    break
                
            if i[:2] == "Ab":
                self.addbefore(i[3:])
            elif i[0] == "A":
                self.append(i[2:])
            elif i[0] == "I":
                self.insert(i[2:])
            elif i[0] == "R":
                self.remove(i[2:])

            straight = self.__str__()
            print("linked list :",straight)

            reverse = self.str_reverse()
            print("reverse :",reverse)




x = input("Enter Input : ").split(",")
lis = DoublyLinkedList()
lis.process(x)
