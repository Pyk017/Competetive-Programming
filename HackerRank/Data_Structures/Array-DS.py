"""
An array is a data structure in which element or data can be stored of same data type in a contiguous block of memory.
Problem : Reversing an Array
"""

n = int(input())
ar = list(map(int, input().split()))
print(*ar[::-1])
