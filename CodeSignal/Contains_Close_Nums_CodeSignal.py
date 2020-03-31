def contains_close_nums(nums, k):
    d = dict()
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = i
        else:
            diff = abs(d[nums[i]] - i)
            if diff <= k:
                return True
            d[nums[i]] = i
    return False

ar = [1, 2, 1]
k = 2
res = contains_close_nums(ar, k)
print(res)