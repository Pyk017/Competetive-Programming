# There are N number of baskets, where the ith basket contains input2[i] apples.
# We want to move apples between baskets so that all baskets have the same number of apples. What is the minimun number of apples that must be
# moved?
# It is guranteed that there exists a way to move apples so as to have an equal number of apples in each basket.

# Input Specification:
# input 1: N, denoting the number of baskets.
# input 2: array representing the number of apples in the ith basket.

# Output :
# Return the minimum number of apples that must be moved so that all baskets have the same number of apples.

# Example 1:

# input 1: 2
# input 2 : [1, 3]

# output : 1

# input 1: 5
# input 2: [2849, 1620, 705, 1, 30]

# output : 2387



def equality(ar, n):
    s = sum(ar) // n
    res = 0
    for i in ar:
        if i > s:
            res += i - s

    return res


n = int(input())
ar = list(map(int, input().split()))
print(equality(ar, n))