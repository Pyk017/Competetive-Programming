def rearrange(arr, n):  # Algorithm taking extra time of O(n).
	temp = [0] * n
	i, j, k = 0, n - 1, 0
	
	flag = True
	while k < n:

		if flag:
			temp[k] = arr[j]
			j -= 1

		else:
			temp[k] = arr[i]
			i += 1

		flag = bool(1 - flag)
		k += 1
	
	return temp


def efficient(arr, n): # in O(1) space complexity.
	max_idx = n - 1
	min_idx = 0

	max_ele = arr[n - 1] + 1

	for i in range(n):
		if i % 2 == 0:
			arr[i] += (arr[max_idx] % max_ele) * max_ele
			
			max_idx -= 1
		else:
			arr[i] += (arr[min_idx] % max_ele) * max_ele
			min_idx += 1
		print(arr[i])
	for i in range(n):
		arr[i] = arr[i] // max_ele

	return arr




arr = list(map(int, input().split()))
# result = rearrange(arr, len(arr))
result = efficient(arr, len(arr))
print(result)