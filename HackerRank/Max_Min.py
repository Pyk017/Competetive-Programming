import sys


def max_min(k, arr):
    arr = sorted(arr)
    maxi = sys.maxsize
    for i in range(len(arr)):
        if i+k-1 < len(arr) and maxi >= arr[i + k - 1] - arr[i]:
            maxi = abs(arr[i + k - 1] - arr[i])

    return maxi


n = int(input())
ki = int(input())
array = [int(x) for x in range(n)]
print(max_min(ki, array))
