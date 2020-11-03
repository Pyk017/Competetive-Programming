"""
Given an array nums of n integers where n > 1. return an array output such that output[i] is equal to the product of all
the elements of nums except nums[i].
Input : [1, 2, 3, 4]
Output : [24, 12, 8, 6]

Note : Please solve it without division and in O(n) time.
"""


import itertools
import operator


def calculate(arr):
    ls = list(itertools.accumulate(arr, operator.mul))
    for i in range(len(arr)):
        arr[i] = int(ls[-1] * (1/arr[i]))

    return arr


array = list(map(int, input("Enter elements in the Array :- ").split()))
print(calculate(array))
