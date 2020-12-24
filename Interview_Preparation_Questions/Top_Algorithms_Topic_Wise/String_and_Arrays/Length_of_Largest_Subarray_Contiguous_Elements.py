def findLength(arr, n):
	max_len = 1
	for i in range(n - 1):
		mx = mn = arr[i]
		myset = set()
		myset.add(arr[i])

		for j in range(i + 1, n):

			if arr[j] in myset:
				break

			myset.add(arr[j])


			mn = min(mn, arr[j])
			mx = max(mx, arr[j])

			if mx - mn == j - i:
				max_len = max(max_len, mx - mn + 1)

	return max_len


arr = list(map(int, input().split()))
n = len(arr)
res = findLength(arr, n)
print(res)
