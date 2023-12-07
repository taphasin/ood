class node:
    def __init__(self,alp,char):
        self.value = ord(alp)
        self.lis = char

def sortin(nod):
    index = 0
    if len(sort) != 0:
        for a in sort:
            if a.value < nod.value:
                index += 1
    sort.insert(index,nod)

input_str = input("Enter Input : ").split()
sort = []
for i in input_str:
    for char in i:
        if char.isalpha():
            h = node(char,i)
            sortin(h)


for b in sort:
    print(b.lis,end=" ")