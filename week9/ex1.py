class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = self.setheight()
    
    def getheight(self,root):
        if root == None:
            return 0
        else:
            return root.height
        
    def setheight(self):
        a = self.getheight(self.left)
        b = self.getheight(self.right)
        return max(a,b)

    def balancevalue(self,root):
        return self.getheight(root.left) - self.getheight(root.right)

    def __str__(self):
        return str(self.val)
  
class AVL_Tree(object): 

    def __init__(self,root = None):
        self.root = root
    
    def insert(self,root,data):
        if root == None:
            return TreeNode(data)
        if root.val < data:
            root.left = self.insert(root.left,data)
        elif root.val > data:
            root.right = self.insert(root.right,data)
            self.rebalance(root)
        return root

    def rebalance(self,root):
        balance = root.balancevalue(root)
        print(balance)
        # if balance == -2:
        #     if root.right.balancevalue() == 1:
        #         rightRotage()
        #     leftRotage()    
        # elif balance == 2:
        #     if root.left.balancevalue() == -1:
        #         leftRotage()
        #     rightRotage()

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("===============")