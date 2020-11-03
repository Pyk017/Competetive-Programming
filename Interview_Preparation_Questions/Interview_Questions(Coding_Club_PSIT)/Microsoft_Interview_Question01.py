# Given non-zero two integers N and M. The Problem is to find number closest to N and divisible by M.
# If there are more than one such number.
# then output the one having the max.absolute value.
# Input: 13, 4 returns 12
# Input: -15, 6 returns -18


def closest(m, n):
    t1, t2 = m, m
    while t1 % n != 0 and t2 % n != 0:
        t1 -= 1
        t2 += 1

    if t1 % n == 0 and t2 % n == 0:
        return t1 if abs(t1) > abs(t2) else t2

    elif t1 % n == 0:
        return t1

    return t2


m = int(input("Enter First Number :- "))
n = int(input("Enter Second Number :- "))
print("Closest Number is :- ", closest(m, n))
