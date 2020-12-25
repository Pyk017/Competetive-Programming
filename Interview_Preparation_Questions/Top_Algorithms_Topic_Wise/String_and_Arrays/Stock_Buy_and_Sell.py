# def stocksSellBuy(stocks, n):
# 	maxcost = 0
# 	min_price = stocks[0]
# 	for i in range(1, n):
# 		min_price = min(min_price, stocks[i])
# 		cost = stocks[i] - min_price

# 		maxcost = max(maxcost, cost)


# 	return maxcost


def stocksSellBuy(stocks, n): 		# using local minima and local maxima
	if n == 1:
		return

	max_cost = 0

	i = 0
	while i < n - 1:
		
		# Finding Local Minima
		while i < n - 1 and stocks[i + 1] <= stocks[i]:
			i += 1

		if i == n - 1:
			break

		buy = i
		i += 1

		# Finding Local Maxima
		while i < n and stocks[i] >= stocks[i - 1]:
			i += 1

		sell = i - 1

		print(buy, sell)
		max_cost += stocks[sell] - stocks[buy]

	return max_cost


stocks = list(map(int, input().split()))
n = len(stocks)
res = stocksSellBuy(stocks, n)
print(res)