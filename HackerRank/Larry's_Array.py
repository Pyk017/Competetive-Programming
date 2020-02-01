for _ in range(int(input())):
    count = 0
    n = int(input())
    ls = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            if ls[i] > ls[j]:
                count += 1

    if count % 2 == 0:
        print('YES')
    else:
        print('NO')
