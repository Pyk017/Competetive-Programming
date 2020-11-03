"""
Given an array of integers, write a function that return true if there exists a triplet (a, b, c) that satisfies
a^2 + b^2 = c^2.
Input : [3, 1, 4, 6, 5]
Output : True
There exists a Pythagorean Triplet (3, 4, 5).
"""


def pythagorean_triplet(a):
    a.sort()
    n = len(a)
    for i in range(n-1, 1, -1):
        j = 0
        k = i-1
        while j < k:
            if a[j] + a[k] == a[i]:
                print(a[j], a[k], a[i])
                return True
            else:
                if a[j] + a[k] < a[i]:
                    j += 1
                else:
                    k -= 1

    return False


ar = list(map(lambda x: x**2, list(map(int, input("Enter elements :- ").split()))))
print(pythagorean_triplet(ar))
