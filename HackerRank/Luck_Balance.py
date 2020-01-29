import heapq


def luck_balance(k, contests):
    ls = []
    sumation = 0
    for i, j in contests:
        if j == 1:
            heapq.heappush(ls, i)

        sumation += i

    for k in range(len(ls) - k):
        sumation -= heapq.heappop(ls)*2

    return sumation


(N, K) = map(int, input().split())
listing = []
for i in range(N):
    a = tuple(map(int, input().split()))
    listing.append(a)

result = luck_balance(K, listing)
print(result)
