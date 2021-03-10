def plusOne(digits):
	digits = ''.join(list(map(str, digits)))
	digits = str(int(digits) + 1)
	return list(map(int, digits))


digits = list(map(int, input().split()))
result = plusOne(digits)
print(result)