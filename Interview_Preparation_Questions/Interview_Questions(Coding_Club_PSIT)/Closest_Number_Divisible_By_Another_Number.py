"""
Find the number closest to n and divisible by m.
Given two integers n and m. The problem is to find the number closest to n and divisible by m. If there are more than
one such number, then output the one having maximum absolute value. If n is completely divisible by m, then output n
only. Time Complexity of O(1) is required.
"""


def find_closest(num, divisor):
    a = num % divisor
    b = divisor - a
    if a == 0 and b == divisor:
        return num + divisor
    if a == b:
        return num + a
    elif a < b:
        return num - a
    else:
        return num + b


n, m = list(map(int, input('Enter n and m :- ').split()))
print("Closest Number is :- ", find_closest(n, m))
