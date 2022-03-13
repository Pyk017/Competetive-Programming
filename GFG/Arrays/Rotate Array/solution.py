class Solution:
    def rotateArr(self,A,D,N):
        P = []
        
        for i in range(D):
            P.append(A[i])

        for i in range(N - D):
            A[i] = A[D + i]

        
        j = N - D

        for k in range(D):
            A[k + j] = P[k]
        
        

nd=[int(x) for x in input().strip().split()]
N=nd[0]
D=nd[1]
A=[int(x) for x in input().strip().split()]
ob=Solution()
ob.rotateArr(A,D,N)

for i in A:
    print(i,end=" ")
    
print()
