def pandemic(arr, n):
    temp = 0
    diff = 0
    count = 0
    for i, j in enumerate(arr):
        if j == 1:
            count += 1
            diff = i - temp
            if diff < 6 and count > 1:
                return 'NO'
            temp = i

    return 'YES'


for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    res = pandemic(ar, n)
    print(res)