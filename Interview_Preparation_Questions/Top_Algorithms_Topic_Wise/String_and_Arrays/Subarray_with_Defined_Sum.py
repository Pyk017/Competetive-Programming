def subarray(arr, n, target):
	start = 0
	curr_sum = arr[0]
	i = 1

	while i <= n:

		while curr_sum > target and start < i - 1:
			curr_sum -= arr[start]
			start += 1

		if curr_sum == target:
			return arr[start: i - 1]

		if i < n:
			curr_sum += arr[i]

		i += 1

	return False


arr = list(map(int, input().split()))
target = int(input())
res = subarray(arr, len(arr), target)
print("No subarray Found") if not res else print(res)