class Solution:
    def sort012(self,arr,n):
        i = 0

        while i < n and arr[i] == 0:
            i += 1
        

        j = i
        
        while j < n:
            while j < n and arr[j] != 0:
                j += 1
                

            if (j < n):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1

        
        k = 0
        while k < n and arr[k] == 0:
            k += 1



        i = k

        while i < n and arr[i] == 1:
            i += 1

        j = i
        
        while j < n:
            while j < n and arr[j] != 1:
                j += 1
                

            if (j < n):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1            


        return arr


    def solution2(self, arr, n):
        digits = [0] * 3

        for i in arr:
            digits[i] += 1;

        for i in range(3):
            for j in range(digits[i]):
                print(i, end=" ")




n = int(input())
arr = [int(x) for x in input().strip().split()]

ob=Solution()


ob.solution2(arr, n)
# ob.sort012(arr,n)

# for i in arr:
#     print(i, end=' ')
# print()

