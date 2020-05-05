def maximize_stock(price):
    profit, current_max = 0, price[-1]
    for i in range(len(price) - 2, -1, -1):
        if price[i] > current_max:
            current_max = price[i]
        else:
            profit += current_max - price[i]
    
    return profit

n = int(input())
ar = list(map(int, input().split()))
print(maximize_stock(ar))
