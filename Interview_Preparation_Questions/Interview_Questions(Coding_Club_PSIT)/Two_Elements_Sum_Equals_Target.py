"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume
that each input would have exactly one solution. and you may not use the same element twice.
Input : [2, 7, 11, 15]
Output : [0, 1]
Explanation : arr[0] + arr[1] = 2 + 7 = 9
"""


def calculate(arr, tar):
    arr.sort()
    i, j = 0, len(arr)-1
    for i in range(len(arr)):
        while i < j:
            if arr[i] + arr[j] == tar:
                return [i, j]
            elif arr[i] + arr[j] < tar:
                i += 1
            else:
                j -= 1
        j = len(arr)-1

    return -1


array = list(map(int, input("Enter elements in the Array :- ").split()))
target = int(input("Enter target element :- "))
print("Found the indices are :- ", calculate(array, target))
