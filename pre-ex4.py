print("*** String Rotation ***")
fst , sst = input("Enter 2 strings : ").split()
first = fst[-2:] + fst[:-2]
second = sst[3:] + sst[:3]
count = 1

while first != fst or second != sst:
    if count <= 5:
        print(count,first,second)
    count += 1
    first = first[-2:] + first[:-2]
    second = second[3:] + second[:3]

if count > 5:
    print(" . . . . . ")
print(count,first,second)
print("Total of ",count,"rounds.")