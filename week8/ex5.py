class Node:
    def __init__(self, data,l = None,r = None):
        self.data = data
        self.left = l
        self.right = r
    
    def __str__(self):
        return str(self.data)
    

class BST:
    
    class stack:
        def __init__(self, q = None):
            if q == None:
                self.item = []
            else:
                self.item = q
        def enstack(self, i):
            self.item.append(i)
        def destack(self):
            first = self.item.pop()
            second = self.item.pop()
            return first,second
        def isEmpty(self):
            return self.item == []
        def size(self):
            return len(self.item)
    
    def __init__(self):
        self.root = None
        self.size = 0
        self.sta = self.stack()

    def insert(self,data):
        if data.isalpha():
            self.sta.enstack(Node(data))
        else:
            tung,tam = self.sta.destack()
            nod = Node(data,tung,tam)
            self.sta.enstack(nod)

    def printTree(self, node, level = 0):
        if node != None:
            it = node.data
            self.printTree(node.left, level + 1)
            print('     ' * level, node)
            self.printTree(node.right, level + 1)

    def inOrder(self,root,rig=0):
        if root is not None:
            if rig == 1:
                print("(",end="")
            self.inOrder(root.right,1)
            print(root, end = '')
            self.inOrder(root.left,2)
            if rig == 2:
                print(")",end="")

    def preOrder(self,root):
        if root is not None:
            print(root, end = '')
            self.preOrder(root.right)
            self.preOrder(root.left)


T = BST()
x = input("Enter Postfix : ")

for i in x:
    lis = T.sta.item
    T.insert(i)

T.root = T.sta.item[0]
print("Tree :")
T.printTree(T.root)
print("--------------------------------------------------")
print("Infix : ",end="")
T.inOrder(T.root)
print("",end="\n")
print("Prefix : ",end="")
T.preOrder(T.root)