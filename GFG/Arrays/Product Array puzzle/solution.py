class Solution:
    def productExceptSelf(self, nums, n):

        if n == 1:            return [1]


        leftProductArray = [0] * n
        rightProductArray = [0] * n

        leftProductArray[0] = nums[0]
        rightProductArray[-1] = nums[-1]
        i = 0

        for i in range(1, n - 1):
             leftProductArray[i] = leftProductArray[i - 1] * nums[i]
             rightProductArray[n - i - 1] = rightProductArray[n - i] * nums[n - i - 1]

        leftProductArray[-1] = leftProductArray[i] * nums[-1]
        rightProductArray[0] = rightProductArray[n - i - 1] * nums[0]
        

        for i in range(n):
            if i == 0:
                nums[i] = rightProductArray[i + 1]
            elif i == n - 1:
                nums[i] = leftProductArray[i - 1]
            else:
                nums[i] = leftProductArray[i - 1] * rightProductArray[i + 1]


        return nums


if __name__ == '__main__':
    n=int(input())
    arr=[int(x) for x in input().split()]

    ans=Solution().productExceptSelf(arr,n)
    print(*ans)
