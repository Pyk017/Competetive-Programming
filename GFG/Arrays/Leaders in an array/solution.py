

class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        result = []
        temp = A[-1]
        j = N - 2
        
        result.append(temp)
        
        while j >= 0:
            if A[j] >= temp:
                result.append(A[j])
                temp = A[j]
                
            j -= 1
            
        return result[::-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


    
def main():    
    N=int(input())
    
    A=[int(x) for x in input().strip().split()]
    obj = Solution()
    
    A=obj.leaders(A,N)
    
    for i in A:
        print(i,end=" ")
    print()
    
    

if __name__=="__main__":
    main()
# } Driver Code Ends