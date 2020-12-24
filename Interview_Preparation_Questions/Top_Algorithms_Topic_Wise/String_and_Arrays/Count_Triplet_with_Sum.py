def triplets(arr, n, target):
	i = 0
	j = n - 1
	k = j - 1

	arr.sort()
	res = 0

	for i in range(n - 2):
		j = i + 1
		k = n - 1
		while j < k:
			if arr[i] + arr[j] + arr[k] >= target:
				k -= 1
			else:
				res += (k - j)	
				j += 1

	return res


arr = list(map(int, input().split()))
target = int(input())
result = triplets(arr, len(arr), target)
print(result)