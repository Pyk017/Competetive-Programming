import heapq


def cars(arr, n):
    heapq._heapify_max(arr)
    i = 0
    x = 0
    r = 0
    while len(arr) > 0:
        x = heapq._heappop_max(arr) - i
        if x >= 0:
            r += x
        i += 1

    return r


for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    res = cars(ar, n)
    print(res)
