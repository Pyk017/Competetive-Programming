def F(x):
    global ar
    i = x + 1
    while i < len(ar):
        if ar[x] < ar[i]:
            return i
        i += 1

    return -1

def G(x):
    if x == -1:
        return None
    global ar
    i = x + 1
    while i < len(ar):
        if ar[x] > ar[i]:
            return i
        i += 1

    return -1


ar = [3, 7, 1, 7, 8, 4, 5, 2]
for i in range(len(ar)):
    try:
        # print(ar[G(F(i))], ar[i], ar[F(i)], ar[G(F(i))])
        print(ar[G(F(i))], end=' ')
    except:
        print(-1, end=' ')
    # print(ar[G(F(i))], end=' ')