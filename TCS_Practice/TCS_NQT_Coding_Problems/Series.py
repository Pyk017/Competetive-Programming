def series(n):
    if n % 2 == 0:
        return (n - 2) // 2
    else:
        return n - 1


num = int(input())
res = series(num)
print(res)
