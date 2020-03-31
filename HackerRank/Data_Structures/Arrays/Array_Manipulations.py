import sys
n, m = map(int, input().split())
ar = [0] * (n + 1)
temp = -sys.maxsize
x = 0
for _ in range(m):
    a, b, k = map(int, input().split())
    ar[a] += k
    if b + 1 <= n:
        ar[b] -= k
for i in range(1, n + 1):
    x += ar[i]
    temp = max(temp, x)
print(temp)
