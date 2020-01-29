<<<<<<< HEAD
"""
Sample Input : 2 3 4'
Output : YES

Input : 2 4
Output : NO

Input : 5 5 5
Output : No
"""


import functools as f


def gcd(x, y):
    while y:
        x, y = y, x % y

    return x


def solve(a):
    if f.reduce(gcd, a) == 1:
        return 'YES'
    return 'NO'


array = list(map(int, input('Enter Array :- ').split()))
print(solve(array))
=======
"""
Sample Input : 2 3 4'
Output : YES

Input : 2 4
Output : NO

Input : 5 5 5
Output : No
"""


import functools as f


def gcd(x, y):
    while y:
        x, y = y, x % y

    return x


def solve(a):
    if f.reduce(gcd, a) == 1:
        return 'YES'
    return 'NO'


array = list(map(int, input('Enter Array :- ').split()))
print(solve(array))
>>>>>>> competetive committed
