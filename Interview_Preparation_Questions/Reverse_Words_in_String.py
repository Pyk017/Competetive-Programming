# Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.

# Input:
# The first line contains T denoting the number of testcases. T testcases follow. Each case contains a string S containing characters.

# Output:
# For each test case, in a new line, output a single line containing the reversed String.

# Constraints:
# 1 <= T <= 100
# 1 <= |S| <= 2000

# Example:
# Input:
# 2
# i.like.this.program.very.much
# pqr.mno

# Output:
# much.very.program.this.like.i
# mno.pqr


for _ in range(int(input())):
    string = input()
    ls = string.split('.')[::-1]
    result = '.'.join(ls)
    print(result)