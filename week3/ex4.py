def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False


class StackCalc:
    def __init__(self, ls = None):
        if ls == None:
            self.items= []
        else:
            self.items = ls
    
    def isEmpty(self):
        return True if len(self.items) > 0 else False

    def push(self,i):
        self.items.append(i)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def run(self, arg):
        arg = arg.split()
        for i in arg:
            if is_number(i):
                self.items.append(i)
            elif i in "+-*/":
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val1 + i + val2)))
            elif i == "DUP":
                val = self.peek()
                self.items.append(val)
            elif i == "POP":
                self.items.pop()
            else:
                self.items = [f"Invalid instruction: {i}"]
                return

    def getValue(self):
        if self.isEmpty():
            if is_number(self.items[0]):
                return int(float(self.peek()))
            else:
                return self.items[0]
        else:
            return 0
                  


print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())