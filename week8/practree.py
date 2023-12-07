class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None
    

class BST:
    def __init__(self):
        self.root = None

    def insert(self,focus,data):
        if focus == None:
            return Node(data)
        if focus.val < data:
            focus.right = self.insert(focus.right,data)
        elif focus.val > data:
            focus.left = self.insert(focus.left,data)
        return focus
    
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node.val)
        printTree90(node.left, level + 1)

def preorder(node):
    if node != None:
        print(node.val,end=" ")
        preorder(node.left)
        preorder(node.right)



def inorder(node):
    if node != None:
        inorder(node.left)
        print(node.val,end=" ")
        inorder(node.right)

def postorder(node):
    if node != None:
        postorder(node)

tree = BST()
root = None
data = input("Enter Input : ").split()
for e in data:
    root = tree.insert(root, e)
    
printTree90(root)
print(root.left.val,root.right.val)
preorder(root)