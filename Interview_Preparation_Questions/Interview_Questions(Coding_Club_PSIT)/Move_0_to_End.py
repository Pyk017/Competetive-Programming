"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
non-zero elements.
Input : [0, 1, 0, 3, 12]
Output : [1, 3, 12, 0, 0]
"""


def movable(arr):
    i, j = 0, len(arr)-1
    while i <= j:
        if arr[i] == 0 and arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[i] != 0 and arr[j] == 0:
            i += 1
            j -= 1
        elif arr[i] != 0 and arr[j] != 0:
            i += 1
        else:
            j -= 1

    return arr


array = list(map(int, input("Enter elements in the Array :- ").split()))
print("New Array is :- ", movable(array))
