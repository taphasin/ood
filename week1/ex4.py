print("*** Fun with Drawing ***")
x = input("Enter input : ")

line = (4 * (int(x) - 1)) + 1
line1 = 0
upside = (int(x) * 2) - 1
downside = upside - 1
air = 0
left_str = ''

for colum in range(upside):
    for left in range(line1):
        if left % 2 == 0:
            print("#",end="")
        else:
            print(".",end="")

    for middle in range(line):
        if colum % 2 == 0:
            print("#",end="")
        else:
            print(".",end="")

    for right in range(line1):
        if right % 2 == 0:
            left_str = left_str + '#'
        else:
            left_str = left_str + '.'

    print(left_str[::-1],end="")
    left_str = ''
    line1 += 1
    line -= 2
    print("\n",end="")

for lower in range(downside):
    left_str = ''
    line1 -= 1
    line += 2
    for left in range(line1):
        if left % 2 == 0:
            print("#",end="")
        else:
            print(".",end="")

    for middle in range(line):
        if lower % 2 == 0:
            print(".",end="")
        else:
            print("#",end="")

    for right in range(line1):
        if right % 2 == 0:
            left_str = left_str + '#'
        else:
            left_str = left_str + '.'

    print(left_str[::-1],end="")
    print("\n",end="")