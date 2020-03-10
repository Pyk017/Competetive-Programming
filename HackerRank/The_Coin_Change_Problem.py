# def change(a, m, n):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 0
#     if m <= 0 and n >= 1:
#         return 0
#     return change(a, m-1, n) + change(a, m, n-a[m-1])


def change(a, m, n):
    table = [0]*(n+1)
    table[0] = 1
    for i in range(m):
        for j in range(a[i], n+1):
            table[j] += table[j - a[i]]
    # print(table)
    return table[n]


N, M = map(int, input().split())
arr = list(map(int, input().split()))
print(change(arr, M, N))
