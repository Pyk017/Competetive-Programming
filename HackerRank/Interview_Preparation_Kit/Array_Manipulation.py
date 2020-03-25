n, m = map(int, input().split())
ls = [0] * (n + 1)
for _ in range(m):
    x, y, k = list(map(int, input().split()))
    ls[x - 1] += k
    if y <= len(ls):
        ls[y] -= k

maxi = x = 0
for i in ls:
    x += i
    maxi = max(maxi, x)

print(maxi)
