close = []
open = []

def match(open, close):
    return (open == '(' and close == ')') or \
        (open == '[' and close == ']')


def parenMatching(str):
    s = str
    i = 0
    while i < len(str):
        c = str[i]
        if c in '[({':
            close.append(c)
        else:
            if c in '])}':
                if len(close) > 0:
                    if match(s.pop(),c):
                        error = 1
                else:
                    error = 2
        i += 1

    if s.size() > 0 and error == 0:
        error = 3
    return error,c,i,s

def match(open, close):
    return (open == '(' and close == ')') or \
        (open == '[' and close == ']')


x = input("Enter Input : ")
sum = 0
print(sum)
if sum == 0:
    print("Perfect ! ! !")