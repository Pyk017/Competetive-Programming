import sys


def max_min(k, arr):
    arr = sorted(arr)
    maxi = sys.maxsize
    for i in range(len(arr)-k+1):
        if arr[i+k-1] - arr[i] < maxi:
            maxi = arr[i+k-1] - arr[i]
    return maxi


n = int(input())
ki = int(input())
array = [int(input()) for _ in range(n)]
print(max_min(ki, array))
