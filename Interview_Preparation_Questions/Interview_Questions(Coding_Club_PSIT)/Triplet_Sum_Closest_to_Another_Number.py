"""
Given an array nums of integers and an integer target, find three integers in nums such that the sum is closest to
target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
Input : [-1, 2, 1, -4]  target = 1
Output : 2
Explanation : The sum that is closest to the target is 2 (-1 + 2 + 1) = 2.
"""


import sys


def triplet(arr, target):
    n = len(arr)
    closest_sum = sys.maxsize
    for i in range(n-1, 1, -1):
        j, k = 0, i-1
        while j < k:
            sui = arr[i] + arr[j] + arr[k]

            if abs(target - sui) < abs(target - closest_sum):
                closest_sum = sui
                
            if sui < target:
                j += 1
            else:
                k -= 1
                
    return closest_sum


array = list(map(int, input("Enter elements in the Array :- ").split()))
tar = int(input("Enter target Element :- "))
print(
    'Closest Sum is :- ', triplet(array, tar)
)
