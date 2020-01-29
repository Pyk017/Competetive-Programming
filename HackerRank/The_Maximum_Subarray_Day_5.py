<<<<<<< HEAD
"""
Sample Input :
2
4
1 2 3 4
6
2 -1 2 3 4 -5

Sample Output :
10 10
10 11

Explanation :
In the first case:
The maximum sum for both types of subsequences is just the sum of all the elements since they are all positive.

In the second case:
The subarray  [2, -1, 2, 3, 4]is the subarray with the maximum sum, and [2, 2, 3, 4] is the subsequence with the maximum sum.
"""


def lis(arr):
    n = len(arr)
    ls = list(arr)
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] >= arr[j] and ls[i] < ls[j] + arr[i]:
                ls[i] = ls[j] + arr[i]

    return max(ls)


def kadane(a):
    max_global = max_current = a[0]
    for i in range(1, len(a)):
        max_current = max(a[i], max_current + a[i])
        if max_current > max_global:
            max_global = max_current

    return max_global


def calc(ls):
    res1 = kadane(ls)
    res2 = lis(ls)
    return [res1, res2]


for i in range(int(input())):
    n = int(input())
    list1 = list(map(int, input().split()))
    print(' '.join(list(map(str, calc(list1)))))
=======
"""
Sample Input :
2
4
1 2 3 4
6
2 -1 2 3 4 -5

Sample Output :
10 10
10 11

Explanation :
In the first case:
The maximum sum for both types of subsequences is just the sum of all the elements since they are all positive.

In the second case:
The subarray  [2, -1, 2, 3, 4]is the subarray with the maximum sum, and [2, 2, 3, 4] is the subsequence with the maximum sum.
"""


def lis(arr):
    n = len(arr)
    ls = list(arr)
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] >= arr[j] and ls[i] < ls[j] + arr[i]:
                ls[i] = ls[j] + arr[i]

    return max(ls)


def kadane(a):
    max_global = max_current = a[0]
    for i in range(1, len(a)):
        max_current = max(a[i], max_current + a[i])
        if max_current > max_global:
            max_global = max_current

    return max_global


def calc(ls):
    res1 = kadane(ls)
    res2 = lis(ls)
    return [res1, res2]


for i in range(int(input())):
    n = int(input())
    list1 = list(map(int, input().split()))
    print(' '.join(list(map(str, calc(list1)))))
>>>>>>> competetive committed
