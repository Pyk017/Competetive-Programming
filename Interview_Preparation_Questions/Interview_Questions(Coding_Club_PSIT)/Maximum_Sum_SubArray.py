"""
Given an integer array nums, find the contiguous sub_arrays (containing at least one number) which has the largest sum
and return its sum.
Input : [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output : 6
Explanation : [4, -1, 2, 1] has the largest sum = 6.
"""


def max_sum(arr):
    max_global = max_current = arr[0]
    for i in range(1, len(arr)-1):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current

    return max_global


array = list(map(int, input("Enter elements :- ").split()))
print("Maximum Sum of Sub Array is :- ", max_sum(array))
