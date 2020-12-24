def smallest(arr, n):
	result = 1
	for i in range(n):
		if arr[i] <= result:
			result += arr[i]
		else:
			break

	return result


arr = list(map(int, input().split()))
n = len(arr)
res = smallest(arr, n)
print(res)