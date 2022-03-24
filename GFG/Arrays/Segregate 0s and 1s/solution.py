class Solution:
    def segregate0and1(self, arr, n):
        i = 0
        while arr[i] == 0:
            i += 1
            
        i += 1
        a = i - 1
        
        for j in range(i, n):
            if arr[j] == 0:
                arr[j], arr[a] = arr[a], arr[j]
                a += 1
                

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    ob.segregate0and1(arr, n)
    print(*arr)
        