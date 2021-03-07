def twoSum(arr, target):
	map = {}
	for i in range(len(arr)):
		temp = target - arr[i]
		if temp in map:
			return [map[temp], i]
		else:
			map[arr[i]] = i


arr = list(map(int, input().split()))
target = int(input())
res = twoSum(arr, target)
print(res)