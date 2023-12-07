class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None

    def getheight(self,x):
        if x == None:
            return -1
        a = self.getheight(x.left)
        b = self.getheight(x.right)
        return 1 + max(a,b)


    def balancevalue(self,root):
        return self.getheight(root.right) - self.getheight(root.left)

    def __str__(self):
        return str(self.val)
  
class AVL_Tree(object): 

    def __init__(self,root = None):
        self.root = root
    
    def insert(self,root,data):
        if root == None:
            return TreeNode(data)
        if root.val < data:
            root.right = self.insert(root.right,data)
        elif root.val > data:
            root.left = self.insert(root.left,data)
        root = self.rebalance(root)
        return root

    def rebalance(self,root):
        balance = root.balancevalue(root)
        print(root,balance)
        if balance < -1:
            print("Not Balance, Rebalance!")
            if root.left.balancevalue(root) > 0:
                root.right = self.rightRotage(root)
            root = self.leftRotage(root)    
        elif balance > 1:
            print("Not Balance, Rebalance!")
            if root.right.balancevalue(root) < 0:
                root.left = self.leftRotage(root)
            root = self.rightRotage(root)
        return root

    def deleteNodeS(self,root : TreeNode, key : int) :
        if root is None : return root
        if int(key) < int(root.val) :
            root.left = self.deleteNodeS(root.left, key)
        elif int(key) > int(root.val) :
            root.right = self.deleteNodeS(root.right, key)
        else :
            if root.left is None or root.right is None :
                root = root.left if root.right is None else root.right
            else :
                temp = root.right
                while temp.left is not None :
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNodeS(root.right, temp.val)
        return root  
        
    
    def leftRotage(self,x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def rightRotage(self,x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    e = int(e)
    print("insert :",e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("===============")

myTree.deleteNodeS(root,2)

printTree90(root)