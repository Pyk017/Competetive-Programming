# You are given an array of n size. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.
# If so, return the integer. If not, return -1. If there are multiple solutions, return any one.
# Input : [1 2 3 1 1]
# Output : 1
# 1 occurs 3 times which is more than 5/3 times.
from collections import Counter
import math


def repeating(a, n):
    d = dict(Counter(a))
    d = sorted(d.items(), key=lambda x: (x[1], x[0]), reverse=True)
    if d[0][1] > math.ceil(len(a) / 3):
        return d[0][0]
    return -1


n = int(input("Enter a number :- "))
print("Enter elements :- ")
a = [int(input()) for i in range(n)]
result = repeating(a, n)
print("Repeating element is :- ", result)
