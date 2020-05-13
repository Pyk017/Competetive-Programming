def nCr(m):
    return m*(m+1)/2

def pairs(a):
    a.sort()
    out = 0
    val = 0
    k = 0
    for i in range(len(a) - 1):
        if a[i] == a[i+1] - 1:
            k += 1
            val = 1
        if a[i] == a[i+1]:
            k += 1
        if a[i] < a[i+1] - 1 or i == n - 2:
            if val == 1:
                out += nCr(k)
                k = 0
                val = 0
            else:
                k = 0
    return int(out)


n = int(input())
ar = list(map(int, input().split()))
res = pairs(ar)
print(res)
