<<<<<<< HEAD
def compute(n):
    dp = [-1] * 10001
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(10001):
        if dp[i] == -1 or dp[i] > dp[i-1] + 1:
            dp[i] = dp[i-1] + 1

        j = 1
        while j <= i and j * i < 10001:
            if dp[j * i] == -1 or dp[i] + 1 < dp[j * i]:
                dp[j * i] = dp[i] + 1
                j += 1

    return dp[n]


num = int(input("Enter Number :- "))
print(compute(num))
=======
def compute(n):
    dp = [-1] * 10001
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(10001):
        if dp[i] == -1 or dp[i] > dp[i-1] + 1:
            dp[i] = dp[i-1] + 1

        j = 1
        while j <= i and j * i < 10001:
            if dp[j * i] == -1 or dp[i] + 1 < dp[j * i]:
                dp[j * i] = dp[i] + 1
                j += 1

    return dp[n]


num = int(input("Enter Number :- "))
print(compute(num))
>>>>>>> competetive committed
