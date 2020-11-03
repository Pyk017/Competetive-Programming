n = int(input())
ar = list(map(int, input().split()))
k = int(input())
d = {i: 0 for i in range(1, max(ar) + 1)}
for i in ar:
	d[i] += 1

for key, value in d.items():
	if value == k:
		break

print(key)
