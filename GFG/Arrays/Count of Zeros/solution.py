class Solution:
    def countZeroes(self, arr, n):
        
        if arr[0] == 0: return n
        
        for idx, val in enumerate(arr[::-1]):
            if val == 1:
                return idx
                
        return 0



if __name__ == '__main__':    
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    ans = ob.countZeroes(arr, n)
    print(ans)
        
