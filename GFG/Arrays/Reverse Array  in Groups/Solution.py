class Solution:
    def reverseInGroups(self, arr, N, k):
        i = 0
        while i < N:
            start = i
            end = min(i + k - 1, N - 1)
            i += k
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1


if __name__ == "__main__":
    nk = [int(x) for x in input().strip().split()]
    N = nk[0]
    K = nk[1]
    arr = [int(x) for x in input().strip().split()]

    ob = Solution()
    ob.reverseInGroups(arr, N, K)
    for i in arr:
        print(i, end=" ")
    print()
