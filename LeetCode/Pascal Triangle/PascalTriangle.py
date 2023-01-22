global pascalTriangle

pascalTriangle = []
pascalTriangle.append([1])
pascalTriangle.append([1, 1])
pascalTriangle.append([1, 2, 1])

evenOdd = lambda x: False if x & 1 else True

for i in range(4, 31):
	if evenOdd(i):
		temp = []
		temp.append(1)
		for j in range(1, ((i - 1) // 2) + 1):
			temp.append(pascalTriangle[i - 2][j] + pascalTriangle[i - 2][j - 1])
		pascalTriangle.append(temp + temp[::-1])
	else:
		temp = []
		temp.append(1)
		for j in range(1, ((i - 1) // 2) + 1):
			temp.append(pascalTriangle[i - 2][j] + pascalTriangle[i - 2][j - 1])
		pascalTriangle.append(temp[:-1] + temp[::-1])


def pascal(rows):
	return pascalTriangle[:rows]
	

rows = int(input())
res = pascal(rows)
print(res)