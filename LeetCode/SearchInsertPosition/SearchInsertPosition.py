def searchInsert(array, target):
	low, high = 0, len(array) - 1
	while low <= high:
		mid = (low + high) // 2
		if array[mid] == target:
			return mid
		elif target > array[mid]:
			low = mid + 1
		else:
			high = mid - 1
	return low


array = list(map(int, input().split()))
target = int(input())
result = searchInsert(array, target)
print(result)