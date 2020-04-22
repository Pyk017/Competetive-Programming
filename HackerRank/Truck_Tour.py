def touring(n, tour):
    fuel = 0
    pump = 0
    for i in range(n):
        fuel += tour[i][0] - tour[i][1]
        if fuel < 0:
            fuel = 0
            pump = i + 1

    return pump


n = int(input())
ls = []
for _ in range(n):
    ls.append(list(map(int, input().split())))

print(touring(n, ls))
