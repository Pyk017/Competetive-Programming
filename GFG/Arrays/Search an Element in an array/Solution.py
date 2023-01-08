class Solution:
    def search(self, arr, N, X):
        for i in range(N):
            if arr[i] == X:
                return i

        return -1


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().strip().split(" ")))
    x = int(input())

    ob = Solution()
    print(ob.search(a, n, x))
