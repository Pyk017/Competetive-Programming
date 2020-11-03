"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n. Find the one that is missing from the array.
Input : [3, 0, 1]
Output : 2

Input : [9, 6, 4, 2, 3, 5, 7, 0, 1]
Output : 8
"""


def find_missing(a):
    count = [0]*(max(a)+1)
    for i in a:
        count[i] += 1

    if 0 in count:
        return a.index(0) + 1
    else:
        return -1


ar = list(map(int, input("Enter array elements :- ").split()))
print("Missing Elements are :- ", find_missing(ar))
