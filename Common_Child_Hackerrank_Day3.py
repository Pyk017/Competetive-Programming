"""
Sample Input :  HARRY
                SALLY
Output : 2
Explanation : The longest String that can be formed by deleting zero or more character from HARRY and SALLY is AY,
                whose length is 2.
Input : AA
        BB
Output : 0
Explanation : AA and BB have no character in common and hence the output is 0.

Input : SHINCHAN
        NOHARAAA
Output : 3
Explanation : The longest string that can be formed between SHINCHAN and NOHARAAA while maintaining the order is NHA.

Input : ABCDEF
        FBDAMN
Output : 2
Explanation : BD is the longest child of the given strings.
"""


def common_child(a, b):
    ls = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                ls[i][j] = ls[i-1][j-1] + 1
            else:
                ls[i][j] = max(ls[i-1][j], ls[i][j-1])

    return ls[len(a)][len(b)]


str1 = input('Enter First String :- ')
str2 = input('Enter Second String :- ')
print(common_child(str1, str2))
