import sys
matrix = [list(map(int, input().split())) for _ in range(6)]
temp = 0
maxi = -sys.maxsize
for i in range(1, 5):
    for j in range(1, 5):
        temp = matrix[i][j] + matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i - 1][j + 1] + matrix[i + 1][j - 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        maxi = max(temp, maxi)
print(maxi) 