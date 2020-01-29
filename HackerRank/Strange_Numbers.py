def strange(la, r):
    array = []
    result = 0
    for i in range(la, r+1):
        if len(str(i)) == 1:
            array.append(i)
            result += 1
        else:
            if i % len(str(i)) == 0:
                a = i // len(str(i))
                if a in array or len(str(a)) == 1:
                    result += 1

                array.append(i)

    return result


for _ in range(int(input())):
    (L, R) = map(int, input().split())
    print(strange(L, R))
