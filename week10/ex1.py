def insertionSort(arr):
    n = len(arr)
    i = 1
    while i < n:
        insert = arr[i]
        ip = i
        while ip > 0 and insert <= arr[ip-1]:
            arr[ip] = arr[ip-1]
            ip -= 1
        arr[ip] = insert
        i += 1
        print("Round",i-1,arr)
    return arr
 
inp = list(map(int, input("Enter list for number: ").split(",")))
print("Before sort:", inp)
inp = insertionSort(inp)
print("After sort:", inp)