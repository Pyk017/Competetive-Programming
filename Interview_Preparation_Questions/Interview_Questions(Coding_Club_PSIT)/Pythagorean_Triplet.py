"""
Given an array of integers, write a function that return true if there exists a triplet (a, b, c) that satisfies
a^2 + b^2 = c^2.
Input : [3, 1, 4, 6, 5]
Output : True
There exists a Pythagorean Triplet (3, 4, 5).
"""


from itertools import combinations
import math


def pythagorean(a):
    ls = list(combinations(a, 2))
    for i in ls:
        if sum(i) in a:
            print(math.sqrt(i[0]), math.sqrt(i[1]), math.sqrt(sum(i)))
            return True

    return False


ar = list(map(lambda x: x**2, list(map(int, input("Enter elements :- ").split()))))
print(pythagorean(ar))
