def jump(a, b, c, d):
    if a < b and c < d:
        return 'NO'
    elif a == c and b == d:
        return 'NO'
    a += b
    c += d
    for i in range(10000):
        if a == c:
            return "YES"

        a += b
        c += d

    return 'NO'


(x1, v1, x2, v2) = map(int, input().split())
print(jump(x1, v1, x2, v2))
