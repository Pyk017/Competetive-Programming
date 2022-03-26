#User function Template for python3

class Solution:
    def findTriplets(self, arr, n):
        arr.sort()
        i, j, k, temp = 0, 0, 0, 0

        for i in range(0, n - 2):
            k = i + 1
            j = n - 1

            while k < j:
                temp = arr[i] + arr[k] + arr[j]
                if (temp == 0):
                    return True
                elif temp < 0:
                    k += 1
                else:
                    j -= 1

                    
        return False






if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().strip().split()))
    if(Solution().findTriplets(a,n)):
        print(1)
    else:
        print(0)
