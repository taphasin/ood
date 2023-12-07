# def bubble(l):
#     for last in range(len(l)-1, 0,-1):
#         swaped = False
#         for i in range(last):
#             if l[i] > l[i+1]:
#                 l[i], l[i+1] = l[i+1], l[i]
#                 swaped = True
#         if not swaped:
#             break











# def bubble(l):
#     for last in range(len(l)-1,0,-1):
#         swap = False
#         for i in range(last):
#             if l[i] > l[i+1]:
#                 l[i],l[i+1] = l[i+1],l[i]
#                 swap = True
#         if not swap:
#             break
























def bub2(l):
    swap = True
    for last in range(len(l)-1,0,-1):
        swap = False
        i = 1
        while i <= last:
            if l[i] < l[i-1]:
                l[i],l[i-1] = l[i-1],l[i]
                swap = True 
            i += 1
        if swap == False:
            break

l = [5,6,2,3,0,1,4]
bub2(l)
print(l)