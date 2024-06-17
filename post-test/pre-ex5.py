class MyInt:
    def __init__(self,num):
        self.num = num
    
    def __add__(self,b):
        return (self.num + b.num) + ((self.num + b.num)/2)
    
    def toRoman(self):
        st = ""
        number = self.num
        if number >= 1000:
            c = int(number/1000)
            st = st + ("M"*c)
            number -= (1000*c)

        if number >= 900:
            c = int(number/900)
            st = st + ("CM"*c)
            number -= (900*c)

        if number >= 500:
            c = int(number/500)
            st = st + ("D"*c)
            number -= (500*c)

        if number >= 400:
            c = int(number/400)
            st = st + ("CD"*c)
            number -= (400*c)

        if number >= 100:
            c = int(number/100)
            st = st + ("C"*c)
            number -= (100*c)

        if number >= 90:
            c = int(number/90)
            st = st + ("XC"*c)
            number -= (90*c)

        if number >= 50:
            c = int(number/50)
            st = st + ("L"*c)
            number -= (50*c)

        if self.num >= 40:
            c = int(number/40)
            st = st + ("XL"*c)
            number -= (40*c)

        if self.num >= 10:
            c = int(number/10)
            st = st + ("X"*c)
            number -= (10*c)
            
        if self.num >= 9:
            c = int(number/9)
            st = st + ("IX"*c)
            number -= (9*c)

        if self.num >= 5:
            c = int(number/5)
            st = st + ("V"*c)
            number -= (5*c)

        if self.num >= 4:
            c = int(number/4)
            st = st + ("IV"*c)
            number -= (4*c)

        if self.num >= 1:
            c = int(number/1)
            st = st + ("I"*c)
            number -= (1*c)

        return f"{self.num} convert to Roman : {st}"

print(" *** class MyInt ***")
x,y = input("Enter 2 number : ").split()

a = MyInt(int(x))

b = MyInt(int(y))

print(a.toRoman())

print(b.toRoman())

print(x,"+",y,"=",int(a+b))