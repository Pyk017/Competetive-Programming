for _ in range(int(input())):
    size = int(input())
    mat = [list(map(int, input().split())) for _ in range(size)]
    count = 0
    res1, res2 = [], []
    for i in range(size):
        for j in range(size):
            count += mat[i][j]

        res1.append(count)
        count = 0
    count = 0
    for i in range(size):
        for j in range(size):
            count += mat[j][i]

        res2.append(count)
        count = 0

    print(res1, res2)
    print("Possible") if sorted(res1) == sorted(res2) else print("Impossible")
