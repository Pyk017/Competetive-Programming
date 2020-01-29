<<<<<<< HEAD
"""
Sample Input :  5 6
                1 2 3 4 1
                3 4 1 2 1 3
Output : 1 2 3
Explanation : There is no common subsequence with length larger than 3. And "1 2 3", "1 2 1", "3 4 1" are all
correct answers.
"""


def lcs(a, b):
    n = len(a) + 1
    m = len(b) + 1
    ls = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if a[i - 1] == b[j - 1]:
                ls[i][j] = ls[i - 1][j - 1] + 1
            else:
                ls[i][j] = max(ls[i - 1][j], ls[i][j - 1])

    i, j = len(a), len(b)
    x = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            x.append(str(a[i - 1]))
            i -= 1
            j -= 1
        elif ls[i - 1][j] > ls[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return x[::-1]


n1, m1 = list(map(int, input().split()))
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
result = ' '.join(list(map(str, lcs(list1, list2))))
print(result)
=======
"""
Sample Input :  5 6
                1 2 3 4 1
                3 4 1 2 1 3
Output : 1 2 3
Explanation : There is no common subsequence with length larger than 3. And "1 2 3", "1 2 1", "3 4 1" are all
correct answers.
"""


def lcs(a, b):
    n = len(a) + 1
    m = len(b) + 1
    ls = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if a[i - 1] == b[j - 1]:
                ls[i][j] = ls[i - 1][j - 1] + 1
            else:
                ls[i][j] = max(ls[i - 1][j], ls[i][j - 1])

    i, j = len(a), len(b)
    x = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            x.append(str(a[i - 1]))
            i -= 1
            j -= 1
        elif ls[i - 1][j] > ls[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return x[::-1]


n1, m1 = list(map(int, input().split()))
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
result = ' '.join(list(map(str, lcs(list1, list2))))
print(result)
>>>>>>> competetive committed
