'''
Sample Input :
abcdaeioub
bbddcc

Sample Output :
aeiou
-1

'''
import sys

check = 'aeiou'
string = input()
temp = ''
maxi = -sys.maxsize
l = -1

for i in range(len(string)):
    if string[i] in check:
        temp += string[i]
        l += 1
    else:
        temp = ''
        l = -1
    maxi = max(maxi, l)
    # print(temp)

print(maxi + 1)