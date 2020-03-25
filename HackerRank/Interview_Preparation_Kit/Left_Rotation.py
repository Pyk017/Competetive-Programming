n, d = map(int, input().split())
ar = list(map(int, input().split()))
for _ in range(d):
    ar.append(ar.pop(0))
print(*ar)