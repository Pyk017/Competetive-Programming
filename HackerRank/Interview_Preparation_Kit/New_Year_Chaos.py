def minimum_bribes(q):
    bribes = 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            return 'Too chaotic'
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    return bribes

for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    res = minimum_bribes(ar)
    print(res)
