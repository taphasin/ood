def simsqrt(num):
	low = 1
	high = num
	while low <= high:
		mid = round((low + high) / 2)
		val = mid * mid
		if val <= num:
			low = mid + 1
		else:
			high = mid - 1
	return high

number = int(input("simple sqrt: "))
print(simsqrt(number))