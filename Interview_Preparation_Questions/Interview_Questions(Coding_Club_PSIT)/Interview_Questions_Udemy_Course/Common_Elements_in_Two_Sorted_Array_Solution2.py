# Given two sorted arrays of number , we need to find the common elements between them.
# Input : [1,3,5,6,7]
#         [1,2,3,7]
# Output : [1,3,7]

def common(a, b):
    i, j = 0, 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            res.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1
    
    return res

A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = common(A, B)
print(*res)
