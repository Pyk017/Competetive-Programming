
class Solution:
    def maxSumPath(self, arr1, arr2, m, n):
        i, j, sumA, sumB, result = 0, 0, 0, 0, 0
        
        while i < m and j < n:
            if (arr1[i] == arr2[j]):
                sumA += arr1[i]
                sumB += arr2[j]
                result += max(sumA, sumB)
                sumA, sumB = 0, 0
                i += 1
                j += 1
                
            if i < m and j < n and arr1[i] < arr2[j]:
                sumA += arr1[i]
                i += 1
                
            if i < m and j < n and arr1[i] > arr2[j]:
                sumB += arr2[j]
                j += 1
                
        while i < m:
            sumA += arr1[i]
            i += 1
            
        while j < n:
            sumB += arr2[j]
            j += 1
            
            
        return result + max(sumA, sumB)

#{ 
#  Driver Code Starts
if __name__=='__main__':
    m,n = list(map(int, input().strip().split()))
    arr1 = list(map(int, input().strip().split()))
    arr2 = list(map(int, input().strip().split()))
    print(Solution().maxSumPath(arr1, arr2, m, n))
