def balancedSum(arr):
    total = sum(arr)
    sum_left = 0
    for i, j in enumerate(arr):
        sum_left += j
        temp_left = total - sum_left - arr[i + 1]
        if temp_left == sum_left:
            return i + 1


array = list(map(int, input().split()))
print(balancedSum(array))
