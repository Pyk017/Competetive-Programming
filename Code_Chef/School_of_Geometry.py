"""
You are given two sequences A1,A2,…,AN and B1,B2,…,BN. You should choose a permutation P1,P2,…,PN of the integers 1
through N and construct N rectangles with dimensions A1×BP1,A2×BP2,…,AN×BPN. Then, for each of these rectangles, you
should construct an inscribed circle, i.e. a circle with the maximum possible area that is completely contained in that
rectangle.

Let S be the sum of diameters of these N circles. Your task is to find the maximum value of S.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test
cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-separated integers A1,A2,…,AN.
The third line contains N space-separated integers B1,B2,…,BN.

Output
For each test case, print a single line containing one integer ― the maximum value of S. It is guaranteed that this
value is always an integer.

Constraints
1≤T≤50
1≤N≤104
1≤Ai,Bi≤109 for each valid i

Subtasks

Subtask #1 (20 points):
A1=A2=…=AN
B1=B2=…=BN

Subtask #2 (80 points):
original constraints

Example Input
2
4
8 8 10 12
15 20 3 5
3
20 20 20
10 10 10

Example Output
30
30
"""
import bisect

for _ in range(int(input())):
    n = int(input())
    A, B = [], []
    str1 = list(map(int, input().split()))
    str2 = list(map(int, input().split()))
    for i, j in zip(str1, str2):
        bisect.insort_left(A, i)
        bisect.insort_left(B, j)

    result = 0
    for i, j in zip(A, B):
        result += min(i, j)

    print(result)
