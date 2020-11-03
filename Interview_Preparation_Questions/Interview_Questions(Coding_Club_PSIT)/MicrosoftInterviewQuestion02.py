# Given an array A consisting of N integers, returns the
# maximum sum of two numbers whose digits add up to an equal
# sum. If there are no two numbers whose digits have an equal
# sum, the function should return -1.

from itertools import combinations


def maximum_sum(it):
    ls = []
    for i, j in it:
        c = sum(list(map(int, [x for x in str(i)])))
        d = sum(list(map(int, [x for x in str(j)])))
        if c == d:
            return c + d

    return -1


array = list(combinations(list(map(int, input("Enter elements in the Array :- ").split(" "))), 2))
print(array)
print("The Maximum Sum is :- ", maximum_sum(array))
