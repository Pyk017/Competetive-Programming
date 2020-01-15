for _ in range(int(input())):
    n = int(input())
    a = int(input())
    s = 5 * (10**(n-1))
    print(s)
    b = int(input())
    c = b + n
    print(c)
    d = int(input())
    e = s - (a + b + c + d)
    print(e)
    if e >= 0:
        print(1)
    else:
        print(-1)
        break
