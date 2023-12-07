num = input("Enter Your List : ").split()
if len(num) <= 2:
    print("Array Input Length Must More Than 2")
    exit()

num = [int(d) for d in num]
x = 1
y = 2
sum_list = []

for a in range(0,len(num)):
    for b in range(x,len(num)):
        for c in range(y,len(num)):
            if num[a] + num[b] + num[c] == 0:
                pre_lis = [num[a],num[b],num[c]]
                pre_lis.sort()
                if pre_lis not in sum_list:
                    sum_list.append(pre_lis)
    y += 1
    x += 1

print(sum_list)