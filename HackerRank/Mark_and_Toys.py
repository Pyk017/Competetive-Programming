n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
count, sumation = 0, 0
for i in range(n):
    if a[i] <= k and sumation + a[i] <= k:
        sumation += a[i]
        count += 1
    else:
        break
print(count)
