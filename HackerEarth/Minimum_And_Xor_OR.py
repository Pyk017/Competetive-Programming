import sys
ar = list(map(int, input().split()))
res = sys.maxsize
for i in range(len(ar)):
    j = i + 1
    temp = (ar[i] & ar[j]) ^ (ar[i] | ar[j])
    res = min(res, temp)
print(res)