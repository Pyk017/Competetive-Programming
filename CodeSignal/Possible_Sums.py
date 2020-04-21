from itertools import combinations

def possibleSums(coins, quantity):
    temp_set = set()
    for i in range(len(coins)):
        for j in range(quantity[i]):
            if not temp_set:
                temp_set.add(coins[i])
            else:
                a = list(map(lambda x: x + coins[i], temp_set))
                temp_set.add(coins[i])
                for k in a:
                    temp_set.add(k)
    #     print(temp_set)

    # print(temp_set)
    return len(temp_set)

    

coin = list(map(int, input().split()))
quant = list(map(int, input().split()))
res = possibleSums(coin, quant)
print(res)













# 50 = 50;
# 10 + 50 = 60;
# 50 + 100 = 150;
# 10 + 50 + 100 = 160;
# 50 + 50 = 100;
# 10 + 50 + 50 = 110;
# 50 + 50 + 100 = 200;
# 10 + 50 + 50 + 100 = 210;
# 10 = 10;
# 100 = 100;
# 10 + 100 = 110.



