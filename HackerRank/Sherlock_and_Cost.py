for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    max1, max2 = 0, 0
    for i in range(1, len(b)):
        current, previous = b[i], b[i-1]
        new_max1 = max(max1 + abs(current - previous), max2 + (current - 1))
        new_max2 = max(max1 + abs(1 - previous), max2)
        max1, max2 = new_max1, new_max2

    print(max(max1, max2))
