def zigZag(arr, n):
	flag = True

	for i in range(n - 1):
		if flag:
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
		else:
			if arr[i] < arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
		flag = bool(1 - flag)

	return arr


arr = list(map(int, input().split()))
n = len(arr)
res = zigZag(arr, n)
print(*res)