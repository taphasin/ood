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
    root = T.insert(i)
print(root.data)
T.printTree(root)