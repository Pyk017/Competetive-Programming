for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    i, j, c = 1, 0, 1
    while i < n:
        if i > 5:
            j = i - 5

        if min(arr[j:i]) > arr[i]:
            c += 1
        i += 1

    print(c)

