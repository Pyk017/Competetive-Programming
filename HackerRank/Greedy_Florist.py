(N, K) = map(int, input().split())
flowers = list(map(int, input().split()))
total = 0
flowers.sort(reverse=True)
for i in range(len(flowers)):
    total += (1 + (i // K)) * flowers[i]

print(total)
