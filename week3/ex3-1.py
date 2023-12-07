class Stack():

    def __init__(self, ls = None):
        if ls == None:
            self.items= []
        else:
            self.items= ls

    def push(self,i):
        self.items.append(i)

    def pop(self):
        if self.isEmpty():
            return self.items.pop()
        else:
            return "$"

    def isEmpty(self):
        return True if len(self.items) > 0 else False

    def size(self):
        pass

def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

def postFixeval(st):

    s = Stack()

    for i in st:
            if is_number(i):
                s.push(i)
            else:
                val1 = s.pop()
                val2 = s.pop()
                s.push(str(eval(val2 + i + val1)))

    return float(s.pop())
            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())


print("Answer : ",'{:.2f}'.format(postFixeval(token)))