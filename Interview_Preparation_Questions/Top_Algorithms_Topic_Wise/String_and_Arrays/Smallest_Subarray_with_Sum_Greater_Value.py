def smallestSubWithSum(arr, n, target):
	curr_sum = 0
	min_len = n + 1

	start, end = 0, 0

	while end < n:
		while curr_sum <= target and end < n:
			curr_sum += arr[end]
			end += 1

		while curr_sum > target and start < n:
			min_len = min(min_len, end - start)
			curr_sum -= arr[start]
			start += 1

	return min_len


arr = list(map(int, input().split()))
target = int(input())
res = subarray(arr, len(arr), target)
print(res)