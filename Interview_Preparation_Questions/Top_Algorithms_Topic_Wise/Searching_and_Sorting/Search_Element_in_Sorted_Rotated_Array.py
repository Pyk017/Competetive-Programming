def searchRotated(arr, l, h, target):
	if l > h:
		return False

	mid = (l + h) // 2
	if target == arr[mid]:
		return mid

	if arr[l] <= arr[mid]:
		if arr[l] <= target <= arr[mid]:
			return searchRotated(arr, l, mid - 1, target)

		return searchRotated(arr, mid + 1, h, target)

	if arr[mid] <= target <= arr[h]:
		return searchRotated(arr, mid + 1, h, target)

	return searchRotated(arr, l, mid - 1, target)



arr = list(map(int, input().split()))
n = len(arr)
tar = int(input())
res = searchRotated(arr, 0, n - 1, tar)
print(res) if res != -1 else print("Not Found!")