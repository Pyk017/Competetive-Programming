class Solution:
    def frequencyCount(self, arr, N, P):
        ans = [0] * N

        for i in range(N):
            value = arr[i]
            if value <= N:
                ans[value - 1] += 1

        for i in range(N):
            arr[i] = ans[i]


    def solution2(self, arr, N, P):
        for i in range(N):
            if arr[i] > N:
                arr[i] = 0

        for i in range(N):
            if arr[i] % (N + 1) > 0:
                arr[(arr[i] % (N + 1)) - 1] += (N + 1)

        for i in range(N):
            arr[i] /= (N + 1)



        
N=int(input())
arr=[int(x) for x in input().strip().split()]
P=int(input())
ob=Solution()
ob.frequencyCount(arr, N, P)
for i in arr:
    print(i, end=" ")
print()
