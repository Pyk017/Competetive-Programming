#User function Template for python3

class Solution:
    def findTriplets(self, arr, n):
        arr.sort()
        print('sorted array')
        print(*arr)
        print()

        i, j, k = 0, n - 1, 0
        temp = 0

        while j > k:
            k = j - 1  
            print(f'i={i}  k={k}  j={j} ') 

            while k > i:
                temp = arr[i] + arr[j] + arr[k]
                print(f'i={i}  k={k}  j={j} ') 
                print(f'temp={temp}')
                if temp == 0:
                    return True

                elif temp < 0:
                    i += 1
                    k = j - 1
                    

                else:

                    k -= 1


            j -= 1


        return False






if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().strip().split()))
    if(Solution().findTriplets(a,n)):
        print(1)
    else:
        print(0)
