x = input("Enter All Bid : ").split()
print(x)

if len(x) <= 1:
    print("not enough bidder")
    exit()

new_int = []
for n in x:
    new_int.append(int(n))

higest = max(new_int)
if new_int.count(higest) > 1:
    print("error : have more than one highest bid")
    exit()

new_int.remove(higest)
higer = max(new_int)

print("winner bid is",higest,"need to pay",higer)