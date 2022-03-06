class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        sum_left = sum(A)
        
        sum_right = 0
        i = N -1
        
        while i >= 0:
            
            sum_left -= A[i]
            
            if sum_left == sum_right: return i + 1
            
            sum_right += A[i]
            
            i -= 1
            
            
        return -1


import math


def main():
    N = int(input())

    A = [int(x) for x in input().strip().split()]
    ob=Solution()

    print(ob.equilibriumPoint(A, N))



if __name__ == "__main__":
    main()
