class TreeNode(object): 
    def __init__(self, val, name): 
        self.val = val 
        self.name = name
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
    
  
class AVL_Tree(object): 

    def __init__(self,root = None):
        self.root = root
    
    def insert(self,root,data,name):
        if root == None:
            return TreeNode(data,name)
        if root.val < data:
            root.right = self.insert(root.right,data,name)
        elif root.val > data:
            root.left = self.insert(root.left,data,name)
        root = self.rebalance(root)
        return root

    def rebalance(self,root):
        balance = root.balancevalue(root)
        if balance < -1:
            if root.left.balancevalue(root.left) > 0:
                root.left = self.rightRotage(root.left)
            root = self.leftRotage(root)    
        elif balance > 1:
            if root.balancevalue(root.right) < 0:
                root.right = self.leftRotage(root.right)
            root = self.rightRotage(root)
        return root
    
    def delete(self, root, key):
        if root is None:
            return root

        if int(key) < int(root.val):
            root.left = self.delete(root.left, key)
        elif int(key) > int(root.val):
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        return self.rebalance(root)

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
            
    
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
    
    def printTree90(self,node, level = 0):
        if node != None:
            self.printTree90(node.left, level + 1)
            print('     ' * level, node.name, node.val)
            self.printTree90(node.right, level + 1)
    
    def preOrder(self,root,level = 0):
        later = False
        if root is not None:
            print("  " * level, root.name, root.val)
            if bool(root.left == None) ^ bool(root.right == None):
                if root.left == None:
                    print("  " * level+1,"*")
                else:
                    later = True
            self.preOrder(root.left,level + 1)
            if later == True:
                print("  " * level+1,"*")
                later = False
            self.preOrder(root.right,level + 1)
    
    
def get_sum_ascii(data):
    res = []
    for ele in data:
        res.extend(ord(num) for num in ele)
    return sum(res)

avl_tree = AVL_Tree()
root = None
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *data = i.split(" ")
    data = data[0] if data else ""
    if op == "I":
        root = avl_tree.insert(root, get_sum_ascii(data),data)
    elif op == "D":
        root = avl_tree.delete(root, get_sum_ascii(data))
    elif op == "P":
        avl_tree.printTree90(root)
        avl_tree.preOrder(root)
        print("------------------------------")
        