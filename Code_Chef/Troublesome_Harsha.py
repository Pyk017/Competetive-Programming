"""
Harsha is hopeless, yet desperate for love. A girl from his class asked him a question. He wants to impress her.
Question is obviously a challenge for him so assigns you the task. He wants your help to solve the question.
The question is, given a number N, she wants to know the sum of, product of elements in a unit ,of all units of the
number N. A unit of number N is defined as a subset formed from the factors of N. As the answer may be large, output it
modulo 10^9+7.

Input
First line contains an integer T indicating the number of test cases.
First line of every test case contains an integer N .

Output
For every test case,print the answer in a new line.

Constraints
1 <= T <= 100000
1 <= N <= 100000

Example
Input
2
4
6

Output
29
167

Explanation

N=4
ans=(1+2+4+1*2+1*4+2*4+1*2*4)%(10^9+7)=29

N=6
ans=(1+2+3+6+1*2+1*3+1*6+2*3+2*6+3*6+1*2*3+1*3*6+2*3*6+1*2*6+1*2*3*6)%(10^9+7)=167
"""

import math


def find_divisors(n):
    res = []
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if n / i == i:
                res.append(i)
            else:
                res.append(i)
                res.append(n // i)

        i += 1

    return res


def products_of_subsets(arr):
    result = 1
    for i in range(len(arr)):
        result *= (arr[i] + 1)

    return result - 1


for _ in range(int(input())):
    num = int(input())
    ar = find_divisors(num)
    print(products_of_subsets(ar) % 1000000007)
