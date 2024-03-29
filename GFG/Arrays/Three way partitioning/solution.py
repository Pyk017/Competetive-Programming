#User function template for Python

class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
    def threeWayPartition(self, array, a, b):
        n = len(array)
        j = 0

        for i in range(n):
            if array[i] < a:
                array[i], array[j] = array[j], array[i]
                j += 1


        for i in range(j, n):
            if array[i] >= a and array[i] <= b:
                array[i], array[j] = array[j], array[i]
                j += 1


        for i in range(j, n):
            if array[i] > b:
                array[i], array[j] = array[j], array[i]
                j += 1


    def betterSolution(self, array, a, b):
        n = len(array)
        start, end = 0, n - 1

        i = 0

        while i <= end:

            if array[i] < a:
                array[start], array[i] = array[i], array[start]
                start += 1
                i += 1

            elif array[i] > b:
                array[end], array[i] = array[i], array[end]
                end -= 1

            else:
                i += 1



from collections import Counter

if __name__=='__main__':
    n = int(input())
    array = list(map(int, input().strip().split()))
    original = Counter(array)
    a,b = list(map(int, input().strip().split()))
    ob = Solution()
    ob.threeWayPartition(array, a, b)

    k1 = k2 = k3 = 0
    for e in array:
        if e > a:
            k3+=1
        elif e<=a and e>=b:
            k2+=1
        elif e<a:
            k1+=1

    m1 = m2 = m3 = 0
    for e in range(k1):
        if array[e]<a:
            m1+=1
    for e in range(k1, k1+k2):
        if array[e]<=a and array[e]>=b:
            m2+=1
    for e in range(k1+k2, k1+k2+k3):
        if array[e]>=a:
            m3+=1

    flag = False
    if k1==m1 and k2==m2 and k3==m3:
        flag = True
    for e in range(len(array)):
        original[array[e]]-=1
    for e in range(len(array)):
        if original[array[e]]!=0:
            flag = False
    if flag:
        print(1)
    else:
        print(0)

# } Driver Code Ends