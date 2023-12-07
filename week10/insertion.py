# def insertion(l):
#     n = 1
#     while len(l) > n:
#         ip = n
#         ele = l[ip]
#         while l[ip] < l[ip-1] and ip > 0:
#             l[ip] = l[ip-1]
#             ip -= 1
#             l[ip] = ele
#         n += 1





















def insertion(l):
    for first in range(1,len(l)):
        ip = first
        ele = l[ip]
        while ip-1 >= 0 and l[ip] < l[ip-1]:
            l[ip] = l[ip-1]
            l[ip-1] = ele
            ip -= 1
        




l = [4,1,5,2,3,7,6,9,8]
insertion(l)
print(l)