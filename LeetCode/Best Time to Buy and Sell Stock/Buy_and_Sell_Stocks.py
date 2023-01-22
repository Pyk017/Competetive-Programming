def maxProfit(prices):
	max_profit = 0;
	min_prices = prices[0]

	for i in range(len(prices)):
		min_prices = min(min_prices, prices[i])
		max_profit = max(max_profit, prices[i] - min_prices)

	return max_profit 


prices = list(map(int, input().split()))
result = maxProfit(prices)
print(result)