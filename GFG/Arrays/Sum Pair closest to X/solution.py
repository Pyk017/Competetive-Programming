import sys

class Solution:
    def sumClosest(self, arr, x):
        ans = []
        i = 0
        j = len(arr) - 1
        temp = 0
        mini = sys.maxsize
        
        while i < j:
            temp = x - (arr[i] + arr[j])
            
            if abs(temp) < mini:
                mini = abs(temp)
                ans = [arr[i], arr[j]]
                
            if temp < 0:
                j -= 1
            else:
                i += 1
                
        return ans




if __name__ == '__main__':
    n, x = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    ans = ob.sumClosest(arr, x)
    print(str(ans[0]) + " " + str(ans[1]))
        
