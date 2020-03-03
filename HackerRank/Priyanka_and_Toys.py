def toys(w):
    containers = 0
    w.sort()
    temp = min(w)
    i = 0
    while w:
        if temp + 4 >= w[i]:
            w.remove(w[i])
        else:
            containers += 1
            temp = w[i]
            w.remove(w[i])

    return containers+1


n = int(input().strip())
array = list(map(int, input().split()))
print(toys(array))
