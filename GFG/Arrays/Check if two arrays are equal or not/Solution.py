class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, A, B, N):

        d = dict()

        for item in A:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1

        for _item in B:
            if _item not in d or d[_item] == 0:
                return False
            d[_item] -= 1

        return True


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    ob = Solution()

    if ob.check(A, B, N):
        print(1)
    else:
        print(0)
