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

    def insert(self,root, data):
        if root == None:
            return Node(data) 
        if root.data > data:
            root.left = self.insert(root.left,data)
        if root.data < data:
            root.right = self.insert(root.right,data)
        return root
    
    def printTree(self, node, level = 0):
        if node != None:
            it = node.data
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
T.size = len(inp)
for i in inp:
    i = int(i)
    T.root = T.insert(T.root,i)
print(T.root.data)
T.printTree(T.root)