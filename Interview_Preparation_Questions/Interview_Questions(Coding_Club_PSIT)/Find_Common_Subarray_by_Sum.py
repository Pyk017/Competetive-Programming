"""
Sample Input:
1 2 3 4 5 0 0 0 6 7 8 9 10
s = 15
Output :
1 8

Explanation :
1+2+3+4+5+0+0+0 = 15
length of this subarray is greater than (4+5+0+0+0+6) whose sum is also 15.
"""

array = list(map(int, input().split()))
s = int(input())
l, r = 0, 0
temp = 0
result = [0]*2

while r < len(array):
    temp += array[r]
    while l < r and temp > s:
        temp -= array[l]
        l += 1
    
    if temp == s and result[1] - result[0] < r - l:
        result = [l+1, r+1]
    
    r += 1
            
    

print(result)
 