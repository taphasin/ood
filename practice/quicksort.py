def quick(l, left, right):
    if left >= right:
        return
    pivot = l[left]
    i, j = left + 1, right
    while i <= j:
        while i <= right and l[i] <= pivot:
            i += 1
        while j > left and l[j] >= pivot:
            j -= 1
        if i < j:
            l[i], l[j] = l[j], l[i]  # Swap
    l[left], l[j] = l[j], l[left]  # Place pivot at its correct position
    quick(l, left, j - 1)  # Sort elements before pivot
    quick(l, j + 1, right)  # Sort elements after pivot


def quicksort(l,left,right):
    if left >= right:
        return
    i,j = left+1, right
    pivot = l[left]
    while i <= j:
        while i <= right and pivot >= l[i]:
            i += 1
        while j > left and pivot <= l[j]:
            j -= 1
        if i < j:
            l[i],l[j] = l[j],l[i]
    l[left],l[j] = l[j],l[left]
    quicksort(l,left,j-1)
    quicksort(l,j+1,right)

lst = [4,5,3]
quicksort(lst, 0, len(lst) - 1)
print(lst)
























