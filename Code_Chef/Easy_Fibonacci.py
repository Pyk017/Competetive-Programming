def fibo(n):
    l = [0, 1]
    for i in range(2, n):
        l.append(l[i-1] + l[i-2])

    return l

def final(l):
    if len(l) == 1:
        return l
    else:
        b = []
        for i in range(1, len(l), 2):
            b.append(l[i])

        return final(b)


for _ in range(int(input())):
    n = int(input())
    l = list(map(str, fibo(n)))
    for i in range(len(l)):
        if len(l[i]) > 1:
            l[i] = l[i][-1]

    l = list(map(int, l))
    print (final(l)[0])



