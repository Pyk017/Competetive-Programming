import sys
def best_index(ar, n):
    acc = []
    acc.append(ar[0])
    for i in range(1, n):
        acc.append(acc[i - 1] + ar[i])
    ans = [0] * (n)
    res = -sys.maxsize
    r = 0
    for i in range(n):
        temp = i
        k = 2
        while temp + k < n:
            temp += k
            k += 1
        if i == 0:
            r = acc[temp]
        else:
            r = acc[temp] - acc[i - 1]

        res = max(res, r)

    return res


n = int(input())
arr = list(map(int, input().split()))
res = best_index(arr, n)
print(res)
    