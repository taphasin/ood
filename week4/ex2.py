class Queue:
    def __init__(self,lst = None):
        if lst == None:
            self.items = []
        else:
            self.items = [x for x in lst]
        self.qone = []
        self.qtwo = []
        self.count = 0
        self.stampo = 2
        self.stampt = 1

    def dequeue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def queue_up(self):
        while self.items != []:
            self.count += 1

            if len(self.qone) > 0:
                if self.stampo == 0:
                    self.qone.pop(0)
                    self.stampo = 3
                self.stampo -= 1


            if len(self.qtwo) > 0:
                if self.stampt == 0:
                    self.qtwo.pop(0)
                    self.stampt = 2
                self.stampt -= 1

            if len(self.qone) < 5 :
                self.qone.append(self.dequeue())
            elif len(self.qtwo) < 5:
                self.qtwo.append(self.dequeue())
            
            print(self.count,self.items,self.qone,self.qtwo)

        

x = input("Enter people : ")
q = Queue(x)
q.queue_up()
