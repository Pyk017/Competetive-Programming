for _ in range(int(input())):
    n, a, b = map(int, input().split())
    x = round((b * n) / (a + b))
    res = a * x**2 + b * (n - x)**2
    print(res)