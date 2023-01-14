def removeElement(array, val):
	while val in array:
		array.remove(val)
	return len(array)


array = list(map(int, input().split()))
val = int(input())
result = removeElement(array, val)
print(result, array[:result])