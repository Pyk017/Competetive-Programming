# You are given an array A of N integers. Now, two functions F(X) and G(X) are defined:
# F(X): This is the smallest number Z, such that X < Z <= N and A[X] < A[Z].
# G(X): This is the smallest number Z, such that X < Z <= N and A[X] > A[Z].

# Now, you need to find for each index i for this array of G(F(i)), where 1 <= i <= N. If such a number does not exist, for a particular
# index i, output -1 as its answer. If such a number does exist, output A[G(F(i))].

# Input:
# The First line contains a single integer N denoting the size of array A. Each of the next lines contains a single integer, where the integer
# on the ith line denotes A[i].

# Output:
# Print N space separated integers on a single line, where the ith integer denotes A[G(F(i))] or -1, if G(F(i)) does not exist.

# Sample Input:
# 8
# 3 7 1 7 8 4 5 2

# Sample Output:
# 1 4 4 4 -1 2 -1 -1

# Explaination:

# Next Greater  Next Smallest
# 3 -> 7          7 -> 1
# 7 -> 8          8 -> 4
# 1 -> 7          7 -> 4
# 7 -> 8          8 -> 4
# 8 -> -1         -1 -> -1
# 4 -> 5          5 -> 2
# 5 -> -1         -1 -> -1
# 2 -> -1         -1 -> -1


def F(x):
    global ar
    i = x + 1
    while i < len(ar):
        if ar[x] < ar[i]:
            return i
        i += 1

    return -1

def G(x):
    if x == -1:
        return None
    global ar
    i = x + 1
    while i < len(ar):
        if ar[x] > ar[i]:
            return i
        i += 1

    return -1


ar = [3, 7, 1, 7, 8, 4, 5, 2]
for i in range(len(ar)):
    try:
        print(ar[G(F(i))], end=' ')
    except:
        print(-1, end=' ')
