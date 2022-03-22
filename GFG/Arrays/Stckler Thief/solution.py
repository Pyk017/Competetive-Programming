class Solution:  
    def FindMaxSum(self,a, n):
        inc, exc = 0, 0
        
        for i in range(n):
            temp = inc
            inc = a[i] + exc
            exc = max(exc, temp)
            print(inc, exc, temp)
            
            
        return max(inc, exc)
        



if __name__ == '__main__':    
    n = int(input())
    a = list(map(int,input().strip().split()))
    ob=Solution()
    print(ob.FindMaxSum(a,n))
# } Driver Code Ends