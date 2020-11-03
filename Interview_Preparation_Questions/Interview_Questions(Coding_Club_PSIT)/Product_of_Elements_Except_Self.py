"""
Given an array nums of n integers where n > 1, returns an array output such that output[i] is equal to the product of all the elements of nums
except nums[i].
Input :
[1, 2, 3, 4]
Ouput :
[24, 12, 8, 6]
"""

array = list(map(int, input().split()))

left_array = [0]*(len(array))
right_array = [0]*(len(array))
left_array[-1] = 1
right_array[0] = 1

for i in reversed(range(len(array)-1)):
    left_array[i] = left_array[i+1]*array[i+1]

for j in range(1, len(array)):
    right_array[j] = right_array[j-1]*array[j-1]

output = [left_array[i]*right_array[i] for i in range(len(array))]
print(*output)
    