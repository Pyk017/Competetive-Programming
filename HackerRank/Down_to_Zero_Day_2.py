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

# Alternative Solution.
"""
N = 10**6

moves = [0] + N * [N]
# print(moves)
for i in range(N):
    moves[i+1] = min(moves[i+1], moves[i] + 1)
    j = 2
    while j <= i and j * i <= N:
        moves[i * j] = min(moves[i * j], moves[i] + 1)
        j += 1

for _ in range(int(input())):
    print(moves[int(input())])
"""



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
