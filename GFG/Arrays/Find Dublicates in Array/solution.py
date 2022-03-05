class Solution:
    def duplicates(self, arr, n): 
        temp = [0] * n
        result = []
        for i in arr:
            temp[i] += 1
            
        for i in range(n):
            if temp[i] > 1:
                result.append(i)
                
        return [-1] if len(result) == 0 else result
                
          
            
         
            
         
            

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends