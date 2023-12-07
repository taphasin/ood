'''
def merge(l, left, right, rightEnd):
	start = left
	leftEnd = right-1
	result = []
	while left <= leftEnd and right <= rightEnd:
		if l[left] < l[right]:
			result.append(l[left])
			left += 1
		else:
			result.append(l[right])
			right += 1
	while left <= leftEnd:
		result.append(l[left])
		left += 1
	while right <= rightEnd:
		result.append(l[right])
		right += 1
	for ele in result:
		l[start] = ele
		start += 1



def mergeSort(l, left, right):
    center = (left+right)//2
    if left < right:
        mergeSort(l, left, center)
        mergeSort(l, center+1, right)
        merge(l, left, center+1, right)
'''	




def merge(l,leftstart,leftend,rightstart,rightend):
    result = []
    start = leftstart
    while leftstart <= leftend and rightstart <= rightend:
        if l[leftstart] < l[rightstart]:
            result.append(l[leftstart])
            leftstart += 1
        else:
            result.append(l[rightstart])
            rightstart += 1
    while leftstart <= leftend:
        result.append(l[leftstart])
        leftstart += 1
    while rightstart <= rightend:
        result.append(l[rightstart])
        rightstart += 1
    for ele in result:
        l[start] = ele
        start += 1
        









def mergeSort(l,left,right):
    center = (left+right)//2
    if left < right:
        mergeSort(l,left,center)
        mergeSort(l,center+1,right)
        merge(l,left,center,center+1,right)









l = [5,3,6,1,2,7,8,4]
mergeSort(l,0, len(l)-1)
print(l)




