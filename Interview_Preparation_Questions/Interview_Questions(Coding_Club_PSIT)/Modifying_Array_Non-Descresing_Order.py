"""
Given an array with n integers, your task is to check if it could become non-descreasing by modifying at most 1 element.
We define an array is non-descreasing if array[i] <= array[i+1] holds for every i (1 <= i < n).
Input : [4, 2, 3, 5]
Output : True
Explanation : You could modify the first 4 to 1 to get a non-descreasing array.

Input : [4, 2, 1]
Output : False
Explanation : You cannot get a non-decreasing array by modify at most one element.
"""


def can_modify(arr):
    count = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            count += 1

    return True if count == 1 else False


array = list(map(int, input("Enter elements in the Array :- ").split()))
print("It can be possible to convert Array to non-decreasing order by modifying 1 element.") if can_modify(array) else \
    print("It cannot be possible.")
