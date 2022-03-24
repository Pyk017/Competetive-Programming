class Solution:
    def hasArrayTwoCandidates(self,arr, n, x):
        mp = dict()
        
        for i in range(n):
            temp = x - arr[i]
            
            if arr[i] in mp:
                return True
            else:
                mp[temp] = arr[i]
                
        return False
                

if __name__ == '__main__':
    n, x = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    ans = ob.hasArrayTwoCandidates(arr, n, x)
    if ans:
        print("Yes")
    else:
        print("No")
