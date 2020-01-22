from collections import *


def solve(dates):
    array = []
    for i, j in dates:
        if j // 10 < i and j % 10 < i:
            array.append((j // 10) * i + j % 10)

    result = 0
    for i in dict(Counter(array)).items():
        result += i[1] * (i[1] - 1) // 2

    return result


listing = []
for _ in range(int(input())):
    listing.append(list(map(int, input().split())))

print(solve(listing))
