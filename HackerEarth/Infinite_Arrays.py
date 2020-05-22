for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    q = int(input())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    s = sum(ar)
    temp = []
    temp.append(0)
    for k in range(len(ar)):
        temp.append(temp[k] + ar[k])
    x = temp[-1]
    for i, j in zip(L, R):
        a = (i - 1) % n
        b = (i - 1) // n
        c = (j - 1) % n
        d = (j - 1) // n
        res = (d - b - 1) * x + temp[c + 1] + x - temp[a]
        print(res % (10**9 + 7), end=' ')
    print(' ')
