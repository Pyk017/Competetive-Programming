import sys

def pairing(arr):
    arr.sort()
    res = sys.maxsize
    r = []
    for i in range(len(arr) - 1):
        x = arr[i]
        y = arr[i + 1]
        diff = abs(y - x)
        
        if diff == res:
            r.append(arr[i])
            r.append(arr[i+1])
        
        elif diff < res:
            res = diff  
            r = []
            r.append(arr[i])
            r.append(arr[i+1])
        
            
    return r
        

n = int(input())
arr = list(map(int, input().split()))
res = pairing(arr)
print(*res)
