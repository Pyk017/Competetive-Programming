'''
Some characters have bounded region and some don't. For Example : 0, 6, a, b, q, etc have 1 bounded region in them, 8, etc have bounded region
and 1, h, k, K, G, etc doesn't have any bounded region.

You are given an paragraph with N words, each word may contain lowercase letters, uppercase letters and number. You have to count the number of
Bounded region in all the words given in the paragraph.

Note : g is considered to have 1 bounded region.

Sample Input :
2
2
hELLo wORlD
8
I have been coding for 48 months now

Sample Output:
4
14
'''

import re
for _ in range(int(input())):
    n = int(input())
    word = input()
    ones = re.findall('[abdegopq490OADRPQ6]', word)
    twos = re.findall('[B8]', word)
    print(ones, twos)
    print(len(ones) + len(twos) * 2)
