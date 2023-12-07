def maxima(input):
    global static
    if len(input) == 0:
        return static
    elif input[-1] >= static:
        static = input[-1]
        input.pop()
        return maxima(input)
    else:
        input.pop()
        return maxima(input)

x = input("Enter Input : ").split()
x = list(map(int,x))
static = x[0]
print("Max :",maxima(x))