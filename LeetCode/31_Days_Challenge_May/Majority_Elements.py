import math
from collections import Counter
def majority(nums):
    ls = dict(Counter(nums))
        for i, j in ls.items():
            if j >= math.ceil(len(nums) / 2):
                return i

arr = list(map(int, input().split()))
print(majority(arr))
