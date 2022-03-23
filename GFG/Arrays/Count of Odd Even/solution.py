import functools 

class Solution:
    def countOddEven(self, arr, n):
        ans = len(list(filter(lambda x: x % 2, arr)))
        
        print(ans, n - ans)



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    obj = Solution()
    obj.countOddEven(arr, n);
