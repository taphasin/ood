def createNone_table():
    global size
    table = []
    for i in range(size):
        table.append(None)
    return table

def isprime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return True
        return False
    return True


def create_table():
    global theshold
    global size
    size = size*2
    while isprime(size):
        size += 1
    table = createNone_table()
    for i in element[0:count-1]:
        table = add(i,table)
    theshold = (size*lim)/100
    return table

def collision(inp,index,colap,table,t):
    global size
    if index >= 0:
        print(f"collision number {colap+1} at {index+(t)**2}")
    if (index+((t+1)**2)) >= size-1:
        index,colap,table = collision(inp,-1,colap,table,0)
    elif table[index+(t+1)**2] != None:
        index,colap,table = collision(inp,index,colap+1,table,t+1)
    else:
        index += (t+1)**2
        colap += 1
    return index,colap,table

def add(inp,table):
    global size
    global theshold
    index = inp % size
    if table[index] != None:
        index,colap,table = collision(inp,index,0,table,0)
        if colap >= max:
            print("****** Max collision - Rehash !!! ******")
            table = create_table()
            index = inp % size
            table[index] = inp
            return table
    table[index] = inp
    return table

def printtable(table):
    cou = 0
    for i in table:
        cou += 1
        print(f"#{cou}	{i}")
    print("----------------------------------------")


print(" ***** Rehashing *****")
property,element = input("Enter Input : ").split("/")
size,max,lim = map(int,property.split())
element = list(map(int,element.split()))
print("Initial Table :")
table = createNone_table()
printtable(table)
count = 0
theshold = (size*lim)/100
for i in element:
    colap = 0
    count += 1
    print(f"Add : {i}")
    if float(count) >= theshold:
        print("****** Data over threshold - Rehash !!! ******")
        table = create_table()
    table = add(i,table)
    printtable(table)
