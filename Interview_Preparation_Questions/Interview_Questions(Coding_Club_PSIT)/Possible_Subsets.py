"""
Given a set of distinct integers, nums, return all possible subsets(the power set). Note: The Solution set must not
contain duplicate subsets.
Input : [1, 2, 3]
Output : [
    [3], [2], [1],
    [1, 2, 3], [1, 3],
    [2, 3], [1, 2],
    []
]
"""


def subsets(array):
    subset = [0]*len(array)
    helper(array, subset, 0)


def helper(array, subset, i):
    if i == len(array):
        print(subset)

    else:
        # subset[i] = []
        helper(array, subset, i+1)
        subset[i] = array[i]
        helper(array, subset, i+1)


arr = list(map(int, input("Enter array elements :- ").split()))
subsets(arr)
