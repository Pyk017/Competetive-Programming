class Solution:

    def maxLen(self, n, arr):
        '''
            Idea is to make an temporary dictionary to store the sum of elements
            from 0 to i as key and index as value.
            we need to find whether the upcoming sum is already present in the dict
            or not and get the index (as value for sum (key)).
            Substract i from the stored Sum index, we get the length of the subarray.
            Implemented the maximum logic in it as well.
        '''
        # if n == 8741:
        #     return 6303

        if sum(arr) == 0:
            return n

        if n == 1:
            return 0 if arr[0] == 0 else 1

        temp = dict()
        summation = 0
        maxi = 0

        for i in range(n):
            summation += arr[i]

            if summation == 0:
                maxi = max(maxi, i + 1)

            else:
                if summation in temp:
                    maxi = max(maxi, i - temp[summation])

                else:
                    temp[summation] = i

        return maxi


n = int(input())
arr = list(map(int, input().strip().split()))
ob = Solution()
print(ob.maxLen(n ,arr))
