def insertion(arr, n):
	key = 0
	for i in range(1, n):
		key = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j -= 1

		arr[j + 1] = key

	return arr


arr = list(map(int, input().split()))
n = len(arr)
result = insertion(arr, n)
print(*result)