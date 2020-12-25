def linearSearch(arr, n, target):
	for i, j in enumerate(arr):
		if j == target:
			return i

	return False


def binarySearch(arr, l, r, target): 	# Recursive Solution
	if r >= l:

		mid = l + (r - 1) // 2

		if arr[mid] == target:
			return mid

		elif arr[mid] > target:
			return binarySearch(arr, l, mid - 1, target)

		else:
			return binarySearch(arr, mid + 1, r, target)

	else:
		return -1


def binarySearch(arr, l, r, target): 	# Iterative Solution
	while l <= r:

		mid = l + (r - 1) // 2

		if arr[mid] == target:
			return mid

		elif arr[mid] > target:
			r = mid - 1

		else:
			l = mid + 1

	return -1


arr = list(map(int, input().split()))
n = len(arr)
target = int(input())

# res = linearSearch(arr, n, target)
# print(res) if res else print("Element not Found!")

res = binarySearch(arr, 0, n - 1, target)
print(res) if res != -1 else print("Element not Found!")