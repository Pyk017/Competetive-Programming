#User function Template for python3
class Solution:

    def findMaximum(self,arr, n):
        i = 0
        
        while i < n - 1 and arr[i] < arr[i + 1]: i += 1
        
        return arr[i]


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    ans = ob.findMaximum(arr, n)
    print(ans)
        
