class Solution:    
    def remove_duplicate(self, A, n):
        i, j, count = 0, 0, 0
        
        while i < n:
            while i < n - 1 and A[i] == A[i + 1]:
                i += 1
                
            i += 1
            j += 1
            
            if i < n and j < n:
                A[j] = A[i]
                
            count += 1
            
        return count


N = int(input())
A = list(map(int, input().strip().split()))
ob = Solution()
n = ob.remove_duplicate(A,N)
for i in range(n):
    print(A[i], end=" ")
print()
