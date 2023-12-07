
# def selection(l):     
#     for last in range(len(l)-1,0,-1):
#         bigest = l[0]
#         big_i = 0
#         for i in range(1,last+1):
#             if bigest < l[i]:
#                 bigest = l[i]
#                 big_i = i
#         l[last],l[big_i] = l[big_i],l[last]
#         print(l[last],l[i])













def selection(l):
    for last in range(len(l)-1,0,-1):
        big = l[0]
        big_i = 0
        i = 0
        while i <= last:
            if l[i] > big:
                big = l[i]
                big_i = i
            i += 1
        l[last],l[big_i] = l[big_i],l[last]








l = [4,1,5,2,3,7,6,9,8]
selection(l)
print(l)










