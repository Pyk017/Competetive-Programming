class Solution:
    def firstRepeated(self,arr, n):
        
        currentMin = n + 1
        mp = dict()
        
        for i in range(n):
            if arr[i] in mp:
                currentMin = min(currentMin, mp[arr[i]])
            else:
                mp[arr[i]] = i
                
        return -1 if currentMin == n + 1 else currentMin + 1
        


if __name__=='__main__':
    n=int(input())
    
    arr=[int(x) for x in input().strip().split()]
    ob = Solution()
    print(ob.firstRepeated(arr, n))
