class find:    
    def finder(self,t,k):
            if t.data == k:
                return t
            if t.left == None and t.right == None:
                print("Not found")
                return
            
            if t.data > k:
                t = t.left
                return self.finder(t,k)
            elif t.data < k:
                t = t.right
                return self.finder(t,k)