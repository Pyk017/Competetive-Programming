class Solution:
    def getPairsCount(self, arr, n, k):
        counter = {i: 0 for i in arr}
        count = 0
        
        for i in arr:
            counter[i] += 1
            
        for i in arr:
            t = k - i
            
            if t in counter:
                counter[i] -= 1
                count += counter[t]
                
        return count


if __name__ == '__main__':
    n, k = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    ans = ob.getPairsCount(arr, n, k)
    print(ans)
