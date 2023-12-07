def remove(string):
    return string.replace(" ", "")

def Queue(st):
    st = remove(st)
    thing = []
    for i in st:
        thing.append(i)
    return thing

def remove(string):
    return string.replace(" ", "")

def encodemsg(word,num):
    en = []
    for w in word:
        if w.islower():
            maxer = 122
        else:
            maxer = 90
        new = chr(ord(w) + int(num[0]))
        if new > chr(maxer):
            new = chr(ord(new) - 26)
        en.append(new)
        num.append(num.pop(0))

    print("Encode message is : ",list(en))
    return en
        


def decodemsg(word,num):
    de = []
    for w in reversed(word):
        if w.islower():
            lowest = 97
        else:
            lowest = 65
        new = chr(ord(w) - int(num[-1]))
        if new < chr(lowest):
            new = chr(ord(new) + 26)
        de.insert(0,new)
        num.insert(0,num.pop())

    print("Decode message is : ",list(de))

x,y = input("Enter String and Code : ").split(",")

q1 = Queue(x)
q2 = Queue(y)


q1 = encodemsg(q1, q2)
decodemsg(q1, q2)