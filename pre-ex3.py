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

"""
lower=0
ls_lower = []
upper=0
ls_upper = []
for i in st:
      if(i.islower()):
            lower+=1
            ls_lower.append(i)
      else:
            upper+=1
            ls_upper.append(i)

            
print("The number of lowercase characters is:",upper)
print("Unique Upper case characters : ",end="")
for i in ls_upper:
      print(i,end=" ")
print("\n",end="")
print("The number of uppercase characters is:",lower)
"""