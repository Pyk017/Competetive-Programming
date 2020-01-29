"""
To help Lavanya learn all about binary numbers and binary sequences, her father has bought her a collection of square
tiles, each of which has either a 0 or a 1 written on it. Her brother Nikhil has played a rather nasty prank.
He has glued together pairs of tiles with 0 written on them. Lavanya now has square tiles with 1 on them and rectangular
 tiles with two 0's on them, made up of two square tiles with 0 stuck together). Thus, she can no longer make all
 possible binary sequences using these tiles.

To amuse herself, Lavanya has decided to pick a number N and try and construct as many binary sequences of length N as
possible using her collection of tiles. For example if N = 1, she can only make the sequence 1. For N=2, she can make
11 and 00. For N=4, there are 5 possibilities: 0011, 0000, 1001, 1100 and 1111.

Lavanya would like you to write a program to compute the number of arrangements possible with N tiles so that she can
verify that she has generated all of them. Since she cannot count beyond 15746, it is sufficient to report this number
modulo 15746.

Input:
A single line with a single integer N.

Output:
A single integer indicating the number of binary sequences of length N, modulo 15746, that Lavanya can make using her
tiles.

Constraints:
You may assume that N≤ 1000000.

Sample Input:
4
Sample Output:
5
"""

n = int(input())
array = [0] * (n + 1)
array[0] = 0
array[1] = 1
array[2] = 2
for i in range(3, n + 1):
    array[i] = (array[i - 1] + array[i - 2]) % 15746

print(array[n])
