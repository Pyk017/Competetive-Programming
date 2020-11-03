"""
Given an array of integers and an integer k, you need to find the total number of continuous sub_arrays whose sum equals
to k.
Input : [1, 1, 1], k = 2
Output : 2
"""


def sub_array(ar, k):
    count = 0
    for i in range(len(ar)):
        temp, j = k, i
        while temp != 0 and j < len(ar):
            if temp >= ar[j]:
                temp -= ar[j]
            j += 1

        if temp == 0:
            count += 1

    return count


array = list(map(int, input("Enter array elements :- ").split()))
s = int(input("Enter Sum :- "))
print("Maximum Continuous Sub-array Sum is :- ", sub_array(array, s))
