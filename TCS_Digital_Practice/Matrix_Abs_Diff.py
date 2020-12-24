def calc_diagonal(mat):
	n = len(mat)
	sumL, sumR = 0, 0
	for i in range(n):
		sumL += mat[i][i]
		sumR += mat[i][n - i - 1]

	return abs(sumL - sumR)


dim = int(input())
mat = [list(map(int, input().split())) for _ in range(dim)]
result = calc_diagonal(mat)
print(result)