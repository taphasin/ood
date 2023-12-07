class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class Linklist:
    def __init__(self):
        self.header = None
        self.trailer = None

def createLL(LL):
    linlis.header = Node("header")
    for i in LL:
        t = linlis.header
        p = Node(i)
        while t.next != None:
            t = t.next
        t.next = p
        linlis.trailer = p
    return linlis.header

def printLL(head):
    t = head.next
    pre_print = ""
    while t != None:
        pre_print = pre_print + " " + t.value
        t = t.next
    return pre_print

def SIZE(head):
    t = head
    count = 0
    while t.next != None:
        count += 1
        t = t.next
    return count

def bottom_up(head,step):
    t = head
    for i in range(step):
        t = t.next
    linlis.trailer.next = linlis.header.next
    linlis.trailer = t
    linlis.header.next = t.next
    t.next = None
    return printLL(linlis.header)

def riffle(head,shuffle):
    t = head.next
    for i in range(shuffle-1):
        t = t.next
    s = head.next
    index = 0
    while linlis.trailer != t and s != t:
        if index % 2 == 0:
            sn = s.next
            ft = t.next
            if t.next != linlis.trailer:
                ftt = t.next.next
            else:
                ftt = None
                linlis.trailer = t
            s.next = ft
            ft.next = sn
            t.next = ftt
            index = 0
        s = s.next
        index += 1
    return printLL(linlis.header)




def scarmble(head, b, r, size):
    round_bottom = int(round(size * b)/ 100)
    round_riffle = int(round(size * r)/100)
    b = float(b)
    r = float(r)
    debot = printLL(linlis.header)
    print("BottomUp {:.3f} % :".format(b),end="")
    print(bottom_up(linlis.header,round_bottom))
    derif = printLL(linlis.header)
    print("Riffle {:.3f} % :".format(r),end="")
    print(riffle(linlis.header,round_riffle))
    print("Deriffle {:.3f} % :".format(r),end="")
    print(derif)
    print("Debottomup {:.3f} % :".format(b),end="")
    print(debot)
    


linlis = Linklist()
inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)

for i in inp2.split('|'):
    h = createLL(inp1.split())
    print("Start :{0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)


# Enter Input : 1 2 3 4 5 6 7 8 9 10/B 30,R 60|B 50,R 50|R 62,B 23
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10
# BottomUp 30.000 % : 4 5 6 7 8 9 10 1 2 3
# Riffle 60.000 % : 4 10 5 1 6 2 7 3 8 9
# Deriffle 60.000 % : 4 5 6 7 8 9 10 1 2 3
# Debottomup 30.000 % : 1 2 3 4 5 6 7 8 9 10