class Solution:   
    def peakElement(self,arr, n):
        
        if n == 1:
            return 0
        
        for i in range(n):
            if i == 0 and arr[i] > arr[i + 1]:
                return i
                
            if i == n - 1 and arr[i] > arr[i - 1]:
                return i
                
            
            if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
                return i
                
        return 0
                

n = int(input())
arr = [int(x) for x in input().split()]

ob = Solution()
result = ob.peakElement(arr, n)
print(result)