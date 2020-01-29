def candy(arr):
    res = [1]*len(arr)
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            res[i] += res[i-1]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > arr[i+1] and res[i] <= res[i+1]:
            res[i] = res[i+1] + 1

    print(res)
    return sum(res)


array = list(map(int, input().split()))
print(candy(array))

# 2 4 2 6 1 7 8 9 2 1
# 1 2 2
# 4 6 4 5 6 2
