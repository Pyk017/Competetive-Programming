def card(m, r, t):
	# m = 2, r = [2, 2], t = 4
	
	ls = [i + 1 for i in range(t)]
	for j in r:
		for i in range(1, t):
			ls[i] = ls[i] + ((j - 1) * (i))
		print(ls)

	return ls[-1]


temp = list(map(int, input().split()))
round_arr = temp[1:-1]
total_round = temp[0]
target = temp[-1]

result = card(total_round, round_arr, target)
print(result)