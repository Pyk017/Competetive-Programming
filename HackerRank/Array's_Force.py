from collections import Counter
for _ in range(int(input())):
    # a1, a2, n, mod = map(int, input().split())
    arr = list(map(int, input().split()))
    d = dict()
    # arr = [a1, a2]
    # d = {a1: 0, a2: 0}
    # for i in range(2, n):
    #     arr[i] = (arr[i - 1] + arr[i - 2]) % mod
    #     if arr[i] not in d:
    #         d[arr[i]] = 0
    #     else:
    #         d[arr[i]] += 1
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]] = 1
        else:
            # print(arr[i])
            d[arr[i]] += 1
    print(d)
    ls = d.values()
    print(ls)
    res = 0
    for i in ls:
        res += i**2
    print(res)
    
    
