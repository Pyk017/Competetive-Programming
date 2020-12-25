def stocks(prices, n):
	if n == 1:
		return 

	i = 0
	while(i < (n - 1)):
		while i < (n - 1) and prices[i + 1] <= prices[i]:
			i += 1
		print(i, prices[i])

		if(i == n - 1):
			break 

		buy = i
		i += 1

		while i < n and prices[i] >= prices[i - 1]:
			i += 1

		sell = i - 1

		print((buy, sell))


prices = list(map(int, input().split()))
stocks(prices, len(prices))
