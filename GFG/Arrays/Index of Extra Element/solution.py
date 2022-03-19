class Solution:
    def findExtra(self,a,b,n):
        for i in range(n):
            if a[i] != b[i]:
                return i
            
            if a[-(i + 1)] != b[-(i + 1)]:
                return n - (i + 1)
            

#{ 
#  Driver Code Starts
if __name__ == "__main__":
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(Solution().findExtra(a,b,n))
# } Driver Code Ends