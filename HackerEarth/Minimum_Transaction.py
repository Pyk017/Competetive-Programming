n, m = map(int, input().split())
ls = [0] * (n + 1)
for _ in range(m):
    u, v, w = map(int, input().split())
    ls[u] += w
    ls[v] -= w

res = 0
for i in ls:
    if i > 0:
        res += i
print(res)
