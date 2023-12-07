raw_x = input("Enter Input: ").split()
sum_min = []
sum_max = []
x = []
for i in raw_x:
    x.append(int(i))

x_findmin = x.copy()
x_findmax = x.copy()

while len(x_findmax) > 1:
    high1 = max(x_findmax)
    x_findmax.remove(high1)
    high2 = max(x_findmax)
    x_findmax.remove(high2)
    sum_max.append(high1 + high2)
    x_findmax.append(high1 + high2)

while len(x_findmin) > 1:
    low1 = min(x_findmin)
    x_findmin.remove(low1)
    low2 = min(x_findmin)
    x_findmin.remove(low2)
    sum_min.append(low1 + low2)
    x_findmin.append(low1 + low2)
    
print("Min cost:",sum(sum_min),"\nMax cost:",sum(sum_max))