def street(input1):
    a, b, c, = 1, 1, 1
    for i in range(input1):
        c = a + b
        a = b
        b = c

    return c * c

num = int(input())
res = street(num)
print(res)