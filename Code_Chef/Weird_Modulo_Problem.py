for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    large = 0
    sum = l[0]
    for i in range(1, len(l)):
        sum %= l[i]
    large = sum
    l = l[::-1]
    sum = l[0]
    for i in range(1, len(l)):
        sum %= l[i]

    large2 = sum

    if large > large2:
        print (large)

    else:
        print (large2)

