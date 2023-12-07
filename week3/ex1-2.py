x = input("Enter Input : ")
li = []
sum = 0


def peek(stack):
    if stack:
        return stack[-1]
    else:
        return None

for i in x:
    li.append(i)

while len(li) > 0:
    last = li.pop()
    if last == ')' and peek(li) == '(':
        li.pop()
    elif last == ']' and peek(li) == '[':
        li.pop()
    else:
        sum += 1

print(sum)
if sum == 0:
    print("Perfect ! ! !")