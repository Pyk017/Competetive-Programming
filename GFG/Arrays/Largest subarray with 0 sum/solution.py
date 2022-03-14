class Solution:
    def maxLen(self, n, arr):
        # temp = [0] * n

        if sum(arr) == 0:
            return n

        temp = dict()
        temp[arr[0]] = 0
        # temp[0] = arr[0]
        t = arr[0]
        maxi = -1

        for i in range(1, n):
            # print(t)
            t += arr[i]
            if t in temp:
                maxi = max(maxi, i - temp[t])
            else:
                temp[t] = i

        # print(temp)
        # print(len(temp))

        # if temp[-1] == 0:
        #     return n
        
        return maxi


n = int(input())
arr = list(map(int, input().strip().split()))
ob = Solution()
print(ob.maxLen(n ,arr))
