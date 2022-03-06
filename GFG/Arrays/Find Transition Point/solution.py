def transitionPoint(arr, n):
    if (arr[0] == 1): return 0
    
    if arr[-1] == 0: return -1
    
    left, right = 0, n - 1;
    
    while (left <= right):
        
        mid = (left + right) // 2
        
        if (arr[mid] == 1 and arr[mid - 1] == 0):
            return mid
            
        if (arr[mid] == 1): 
            right = mid - 1
            
        if (arr[mid] == 0):
            left = mid + 1
            
    return -1;
        
    
n = int(input())
arr = list(map(int, input().strip().split()))
print(transitionPoint(arr, n))
