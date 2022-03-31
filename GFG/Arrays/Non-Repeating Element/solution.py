class Solution:
    def firstNonRepeating(self, arr, n): 
        d = dict()
        
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
        for i in arr:
            if d[i] == 1:
                return i
                
        return 0


from collections import defaultdict 

n = int(input())
arr = list(map(int,input().strip().split()))
ob = Solution()
print(ob.firstNonRepeating(arr, n))
