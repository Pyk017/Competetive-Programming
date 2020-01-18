"""
One of the teachers from CSE department did not agree for mass bunk during Pongal. After repeated requests from
students, he told that he would accept for the bunk if everyone solves this question.

The question is as follows:
Given a number N, which is the size of array where indices are from 1 to N . Initially all the elements of array are 0 .
Q queries are given . Each query contains two variables L and R . For each query you have to perform the following
operation : for each index i where L<=i<=R you have to add a value of of (i-L+1) to the array element at index i .
After performing Q queries, a number M is given. It is followed by M number of indices (I) where, for each index you
have to output the value of element present in that index (I) of array.

Input
First line contains an integer N indicating the size of array indexed from 1 to N.
Second line contains an integer Q denoting the number of Queries.
It is followed by Q number of lines where each line contains two space seperated integers L and R.
Next Line contains an Integer M denoting number of queries whose output is to be printed.
It is followed by M number of lines where each line contains an integer I (index of element in array).

Output
For each of the M queries, output the value of element present in the array at index I.

Constraints
1 <= N <= 1000000
1 <= Q <= 1000000
1 <= L <= R <= N
1 <= M <= N

Example
Input:
5
3
1 3
2 4
1 5
3
1
3
5

Output:
2
8
5
"""


n = int(input())

arr_1 = [0 for _ in range(n+1)]
arr_2 = [0 for _ in range(n+1)]

for _ in range(int(input())):
    (L, R) = map(int, input().split())
    L -= 1
    arr_1[L] += 1
    arr_1[R] -= 1
    arr_2[R] += (R - L)

result = [0 for _ in range(n+1)]
result[0] = arr_1[0] - arr_2[0]
for i in range(1, n):
    arr_1[i] += arr_1[i-1]
    result[i] = result[i-1] + arr_1[i] - arr_2[i]

print(result, arr_2, arr_1)
for _ in range(int(input())):
    print(result[int(input()) - 1])
