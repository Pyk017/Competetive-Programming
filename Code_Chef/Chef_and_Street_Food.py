for _ in range(int(input())):
    n = int(input())
    profit = 0
    for _ in range(n):
        s,p,v = [int(i) for i in input().split()]
        profit = max(v * (p//(s+1)), profit)
    print(profit)

