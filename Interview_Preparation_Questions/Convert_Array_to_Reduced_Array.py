def convert(a):
    b = sorted(a)
    c = []
    for i in a:
        c.append(b.index(i))
    return c

for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    res = convert(ar)
    print(*res)