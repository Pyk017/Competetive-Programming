def containsDuplicate(nums):
	return len(nums) != len(set(nums))


arr = list(map(int, input().split()))
result = containsDuplicate(arr)
print(result)
