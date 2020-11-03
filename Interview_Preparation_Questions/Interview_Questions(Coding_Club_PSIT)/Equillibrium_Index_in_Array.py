"""
Equilibrium index of an array is an index i such that the sum of elements at indices less than is equal to the sum of
elements at indices greater than i. Find and return the equilibrium index of an array. Element at index is not included
in either part. And return -1 if no equilibrium index is present.

Time Complexity : O(n)
Space Complexity : O(n)

Input :  3 11 15 12 6 13 10
Output : 3
"""


def equilibrium(array):
    left_sum, sumi = 0, sum(array)
    for i in range(len(array)):
        sumi -= array[i]
        if left_sum == sumi:
            return i

        left_sum += array[i]

    return -1


numbers = list(map(int, input().split()))
print(equilibrium(numbers))
