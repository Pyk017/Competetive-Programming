<<<<<<< HEAD
"""
Sample Input : 5(size of first Array),  4(size of second Array),  10(value of x)
                4 2 4 6 1
                2 1 8 5
Output : 4
Explanation : [4, 2, 2, 1]
"""


def two_stack(x, a, b):
    i, j, su, count, n, m = 0, 0, 0, 0, len(a), len(b)
    while i < n and su + a[i] <= x:
        su += a[i]
        i += 1

    count = i
    while j < m and i >= 0:
        su += b[j]
        j += 1

        while su > x and i > 0:
            i -= 1
            su -= a[i]

        if su <= x and i + j > count:
            count = i + j

    return count


array_1 = list(map(int, input("Enter First Array :- ").strip().split()))
array_2 = list(map(int, input("Enter Second Array :- ").strip().split()))
target = int(input("Enter target element :- "))
print(two_stack(target, array_1, array_2))
=======
"""
Sample Input : 5(size of first Array),  4(size of second Array),  10(value of x)
                4 2 4 6 1
                2 1 8 5
Output : 4
Explanation : [4, 2, 2, 1]
"""


def two_stack(x, a, b):
    i, j, su, count, n, m = 0, 0, 0, 0, len(a), len(b)
    while i < n and su + a[i] <= x:
        su += a[i]
        i += 1

    count = i
    while j < m and i >= 0:
        su += b[j]
        j += 1

        while su > x and i > 0:
            i -= 1
            su -= a[i]

        if su <= x and i + j > count:
            count = i + j

    return count


array_1 = list(map(int, input("Enter First Array :- ").strip().split()))
array_2 = list(map(int, input("Enter Second Array :- ").strip().split()))
target = int(input("Enter target element :- "))
print(two_stack(target, array_1, array_2))
>>>>>>> competetive committed
