def permute(ans):
	n = len(nums)
	ans = [0] * n

    for i in range(n):
        ans[i] = nums[nums[i]]

    return ans



array = list(map(int, input().split()))
result = permute(array)
print(*result)


10
5 0 2 1 3 2 4 9 8 10
2 6

9
76 8 75 22 59 96 30 38 36
44 62