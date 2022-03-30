class Solution:
    def rearrange(self,arr, n):
        
        positive = [x for x in arr if x >= 0]
        negative = [x for x in arr if x < 0]
        
        i, j, k = 0, 0, 0
        n, m = len(positive), len(negative)
        
        while i < n and j < m:
            if k % 2 == 0:
                arr[k] = positive[i]
                i += 1
                
            else:
                arr[k] = negative[j]
                j += 1
                
            k += 1
                
        
        while i < n:
            arr[k] = positive[i]
            i += 1
            k += 1
            
        while j < m:
            arr[k] = negative[j]
            j += 1
            k += 1
                    


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    ob.rearrange(arr, n)
    for x in arr:
        print(x, end=" ")
    print()
