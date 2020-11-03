# You are standing on a point (n, m) and you want to go to origin (0, 0) by taking steps either left or down i.e. from each point you are allowed to move either in (n-1, m) or (n, m-1). Find the number of paths from point to origin.

# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two integers n and m representing the point.

# Output:
# For each testcase, in a new line, print the total number of paths from point to origin.

# Constraints:
# 1 <= T<= 100
# 1 <= n, m <= 25

# Example:
# Input:
# 3
# 3 2
# 3 6
# 3 0

# Output:
# 10
# 84
# 1

def paths(n, m):
    if n == 0 or m == 0:
        return 1
    return paths(n - 1, m) + paths(n, m - 1)


for _ in range(int(input())):
    n, m = map(int, input().split())
    res = paths(n, m)
    print(res)
    