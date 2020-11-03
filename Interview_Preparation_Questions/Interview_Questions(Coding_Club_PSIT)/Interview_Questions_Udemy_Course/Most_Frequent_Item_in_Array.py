# Given an list of number and we need to return the most frequent occuring item in the list.
# Input : [1,3,1,3,2,1]
# Output : 1

def most_frequent(arr):
    di = {}
    r = 0
    for i in arr:
        if  i not in di:
            di[i] = 0
        else:
            di[i] += 1
            if di[i] > r:
                r = di[i]
                ans = i

    return ans

 
arr = list(map(int, input().split()))
res = most_frequent(arr)
print(res)
