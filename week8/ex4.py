class Queue:
    def __init__(self, q = None):
        if q == None:
            self.item = []
        else:
            self.item = q
    def enQueue(self, i):
        self.item.append(i)
    def deQueue(self):
        return self.item.pop(0)
    def isEmpty(self):
        return self.item == []
    def size(self):
        return len(self.item)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data):
        if self.root == None:
            self.root = Node(data) 
            return
        t = self.root
        for i in range(self.size):
            if t.data > data:
                if t.left == None:
                    t.left = Node(data)
                    return self.root
                t = t.left
            if t.data < data:
                if t.right == None:
                    t.right = Node(data)
                    return self.root
                t = t.right
        
        print("BUG")
        exit()
    
    def leverOrder(self):
        q = Queue()
        q.enQueue(self.root)
        while q.isEmpty() is not True :
            n = q.deQueue()
            print(n.data, end = ' ')
            if n.left is not None:
                q.enQueue(n.left)
            if n.right is not None:
                q.enQueue(n.right)

    def inOrder(self,root):
        if root is not None:
            self.inOrder(root.left)
            print(root, end = ' ')
            self.inOrder(root.right)
    
    def preOrder(self,root):
        if root is not None:
            print(root, end = ' ')
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self,root):
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root, end = ' ')

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
T.size = len(inp)
for i in inp:
    root = T.insert(i)

print("Preorder : ",end="")
T.preOrder(T.root)

print("\nInorder : ",end="")
T.inOrder(T.root)

print("\nPostorder : ",end="")
T.postOrder(T.root)

print("\nBreadth : ",end = "")
T.leverOrder()