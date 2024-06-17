print(" *** String count ***")
st = input("Enter message : ")

lower=0
ls_lower = []
upper=0
ls_upper = []

i = 69
while i <= 70:
    for a in st:
        if a == i:
            ls_upper.append(a)
            upper += 1
            break
        print(i)
print(upper)
