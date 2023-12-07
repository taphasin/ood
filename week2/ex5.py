class funString():

    def __init__(self,st):
        self.string = st

    def size(self) :
        return len(self.string)

    def changeSize(self):
        x = ""
        for i in self.string:
            if 'a' <= i <= 'z':
                x += i.upper()
            else:
                x += i.lower()
        return x

    def reverse(self):
        return self.string[::-1]

    def deleteSame(self):
        return "".join(dict.fromkeys(self.string))



str1 , str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())