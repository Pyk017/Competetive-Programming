# Given two sorted arrays of number , we need to find the common elements between them.
# Input : [1,3,5,6,7]
#         [1,2,3,7]
# Output : [1,3,7]

def common(a, b):
    di = {i: 0 for i in a}
    res = []
    for j in b:
        try:
            di[j] += 1
            res.append(j)
        except:
            continue
    
    return res

A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = common(A, B)
print(*res)
