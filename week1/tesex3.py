class MyInt:
    def __init__(self,num):
        self.num = num
    
    def __add__(self,b):
        return (self.num + b.num) + ((self.num + b.num)/2)
    
    def toRoman(self):
        st = ""
        number = self.num
        if number >= 1000:
            c = int(number / 1000)
            st = st + ("M"*c)
            number -= (1000*c)
        return st

print(" *** class MyInt ***")
x,y = input("Enter 2 number : ").split()

a = MyInt(int(x))

b = MyInt(int(y))

print(a.toRoman())

print(b.toRoman())

print(x,"+",y,"=",int(a+b))