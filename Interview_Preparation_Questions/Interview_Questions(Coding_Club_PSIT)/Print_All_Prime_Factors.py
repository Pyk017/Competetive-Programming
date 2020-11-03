"""
Given a number n find all the prime factors of a number in a most optimised way.

Input : 54
Output : [2, 3, 3, 3]

Input : 120
Output : [2, 2, 2, 3, 5]
"""
import math


def prime_factor(n):
    ls = []
    while n % 2 == 0:
        ls.append(2)
        n /= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            ls.append(i)
            n /= i

    if n > 2:
        ls.append(int(n))

    return ls


num = int(input("Enter a Number :- "))
print("All Prime Factors of Number is :- ", prime_factor(num))
