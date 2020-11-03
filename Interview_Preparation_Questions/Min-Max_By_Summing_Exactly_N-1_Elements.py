'''
Given N positive integers, Find the Minimum and Maximum values that can be calculated by Summing Exactly N-1 of the N integers. Then Print 
the respective minimum and maximum values as a single line of two space separated integers.

Sample Input : 
5
8 7 2 4 5

Sample Output : 
18 24

'''
import sys

n = int(input())
ar = list(map(int, input().split()))
mini = sys.maxsize
maxi = -sys.maxsize
s = 0

for i in ar:
    mini = min(mini, i)
    maxi = max(maxi, i)
    s += i

print(s - maxi, s - mini)