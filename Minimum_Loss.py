import sys


def get_key(item):
    return item[0]


def minimum_loss(d):
    d.sort(key=get_key, reverse=True)
    min_loss = sys.maxsize
    for i in range(n - 1):
        if (d[i][0] - d[i + 1][0]) < min_loss and d[i][1] < d[i + 1][1]:
            min_loss = d[i][0] - d[i + 1][0]

    return min_loss


n = int(input())
numbers = list(map(int, input().split()))
dig = []
for j in range(len(numbers)):
    dig.append((numbers[j], j + 1))

print(minimum_loss(dig))
