class Solution:
    def convertToWave(self,arr,N):        
        for i in range(0, N - 1, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        


import math
        
N=int(input())

A=[int(x) for x in input().split()]
ob=Solution()
ob.convertToWave(A,N)
for i in A:
    print(i,end=" ")

print()
