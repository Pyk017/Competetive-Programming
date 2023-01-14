class Solution:
    def firstElementKTime(self,  a, n, k):
        mp = dict()
        for item in a:
            if item in mp:
                mp[item] += 1
            else:
                mp[item] = 1

            if mp[item] == k:
                return item

        return -1


if __name__ == "__main__":
    sx = [int(x) for x in input().strip().split()]
    n, k = sx[0], sx[1]
    arr = [int(x) for x in input().strip().split()]
    ob = Solution()
    print(ob.firstElementKTime(arr, n, k))
