sumall = 1
def count_left(st,index):
    global sumall
    if len(st) <= index or index < 0 or st[index] != thatchar:
        return
    if st[index] == thatchar:
        sumall += 1
        count_left(st,index+1)
    return

def count_right(st,index):
    global sumall
    if len(st) <= index or index < 0 or st[index] != thatchar:
        return
    if st[index] == thatchar:
        sumall += 1
        count_right(st,index-1)
    return


st,index = input("input number : ").split(",")
index = int(index)-1
if st is '':
    print("Output : List is entry")
    exit()

if len(st) <= index:
    print("Output : Pin number out of range")
    exit()

if index < 0:
    print("Output : Pin number less than 1")
    exit()

thatchar = st[index]
count_left(st,index+1)
count_right(st,index-1)
print("Character :",thatchar)
print("Count :",sumall)
