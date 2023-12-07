class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree(object):
    def __init__(self, root=None):
        self.root = root

    def insert(self, root, data):
        if root is None:
            return TreeNode(data)
        if data < root.val:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        # Update the height of the current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Rebalance the tree
        return self.rebalance(root)

    def get_height(self, x):
        if x is None:
            return 0
        return x.height

    def balance_value(self, root):
        if root is None:
            return 0
        return self.get_height(root.right) - self.get_height(root.left)

    def rebalance(self, root):
        balance = self.balance_value(root)

        # Left Heavy
        if balance < -1:
            print("Not Balance, Rebalance!")
            if self.balance_value(root.left) > 0:
                root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Heavy
        if balance > 1:
            print("Not Balance, Rebalance!")
            print(print_tree_90(root))
            if self.balance_value(root.right) < 0:
                root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        x.right = y

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

def print_tree_90(node, level=0):
    if node is not None:
        print_tree_90(node.right, level + 1)
        print('     ' * level, node.val)
        print_tree_90(node.left, level + 1)

myTree = AVL_Tree()
root = None

data = input("Enter Input : ").split()
for e in data:
    e = int(e)
    print("insert :", e)
    root = myTree.insert(root, e)
    print_tree_90(root)
    print("===============")
