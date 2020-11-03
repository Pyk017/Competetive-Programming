"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets
in the array which gives the sum of zero.
Note : The solution set must not contain duplicate triplets.
Input : [-1, 0, 1, 2, -1, -4]
Output : [[-1, 0, 1], [-1, -1, 2]]
"""


def triplet(arr):
    arr.sort()
    result = []
    for i in range(len(arr)-1, 1, -1):
        j, k = 0, i-1
        while j < k:
            if arr[j] + arr[k] == -arr[i]:
               result.append([arr[j], arr[k], arr[i]])
               break
            elif arr[j] + arr[k] < -arr[i]:
                j += 1
            else:
                k -= 1
    ls = []
    for i in result:        # To remove Redundancy.
        if i not in ls:
            ls.append(i)

    return ls


array = list(map(int, input("Enter elements in the Array :- ").split()))
print("Unique Triplet equals to zero is :- ", triplet(array))
