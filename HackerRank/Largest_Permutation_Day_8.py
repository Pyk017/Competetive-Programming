<<<<<<< HEAD
"""
Sample Input :
5 1
4 2 3 5 1

Sample Output :
5 2 3 4 1

Explanation :
You can swap any two numbers [4, 2, 3, 5, 1] in  and see the largest permutation is [5, 2, 3, 4, 1].

Sample Input 1
3 1
2 1 3

Sample Output 1
3 1 2

Explanation 1
With 1 swap we can get [1, 2, 3], [3, 1, 2]  and [2, 3, 1]. Of these, [3, 1, 2] is the largest permutation.

Sample Input 2
2 1
2 1

Sample Output 2
2 1

Explanation 2
We can see that [2, 1] is already the largest permutation. We don't make any swaps.
"""


def permute(a, k):
    n = len(a)
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i
    j = 0
    while k > 0 and j < n:
        if a[j] != n - j:
            temp = a[j]
            pos = b[n - j - 1]
            a[j] = a[pos]
            a[pos] = temp

            b[n - j - 1] = j
            b[temp - 1] = pos
            k -= 1

        j += 1

    return a


n, k = list(map(int, input().split()))
ls = list(map(int, input().split()))
print(' '.join(list(map(str, permute(ls, k)))))
=======
"""
Sample Input :
5 1
4 2 3 5 1

Sample Output :
5 2 3 4 1

Explanation :
You can swap any two numbers [4, 2, 3, 5, 1] in  and see the largest permutation is [5, 2, 3, 4, 1].

Sample Input 1
3 1
2 1 3

Sample Output 1
3 1 2

Explanation 1
With 1 swap we can get [1, 2, 3], [3, 1, 2]  and [2, 3, 1]. Of these, [3, 1, 2] is the largest permutation.

Sample Input 2
2 1
2 1

Sample Output 2
2 1

Explanation 2
We can see that [2, 1] is already the largest permutation. We don't make any swaps.
"""


def permute(a, k):
    n = len(a)
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i
    j = 0
    while k > 0 and j < n:
        if a[j] != n - j:
            temp = a[j]
            pos = b[n - j - 1]
            a[j] = a[pos]
            a[pos] = temp

            b[n - j - 1] = j
            b[temp - 1] = pos
            k -= 1

        j += 1

    return a


n, k = list(map(int, input().split()))
ls = list(map(int, input().split()))
print(' '.join(list(map(str, permute(ls, k)))))
>>>>>>> competetive committed
