class Solution:
    def findSwapValues(self,a, n, b, m):
        a.sort()
        b.sort()
        sum_a = sum(a)
        sum_b = sum(b)
        
        i, j = 0, 0
        
        while i < n and j < m:
            x = sum_a - a[i] + b[j]
            y = sum_b - b[j] + a[i]
            
            if x == y: 
                return 1
            
            if x > y: 
                i += 1
            
            else: 
                j += 1
            
        return -1
            

#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    l=list(map(int,input().split()))
    n=l[0]
    m=l[1]
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    ob = Solution()
    print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends