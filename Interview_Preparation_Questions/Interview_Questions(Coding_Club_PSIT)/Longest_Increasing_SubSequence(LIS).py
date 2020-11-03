"""
Given an unsorted array of integers, find the length of longest increasing subsequence.
Input : [10, 9, 2, 5, 3, 7, 101, 18]
Output : 4
Explanation : The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
"""


def lis(arr):
    n = len(arr)
    ls = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and ls[i] < ls[j] + 1:
                ls[i] = ls[j] + 1

    return max(ls)


array = list(map(int, input("Enter elements in the Array :- ").split()))
print('Length of Longest Increasing Sub-Sequence is :- ', lis(array))
