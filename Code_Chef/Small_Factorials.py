"""
You are asked to calculate factorials of some small positive integers.

Input
An integer t, 1<=t<=100, denoting the number of test cases, followed by t lines, each containing a single integer n,
1<=n<=100.

Output
For each integer n given at input, display a line with the value of n!

Example
Sample input:
4
1
2
5
3
Sample output:

1
2
120
6
"""
import functools as f
import operator as op


def factorial(n):
    return f.reduce(op.mul, range(1, n+1))


for _ in range(int(input())):
    print(factorial(int(input())))
