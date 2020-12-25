import math

def prime(n):
    if n <= 1:
        return False

    elif n == 2:
        return True

    w = int(math.sqrt(n))
    for i in range(2, w + 1):
        if n % i == 0:
            return False

    return True


def check(n):
    if n < 0:
        return "Enter valid number !"
    else:
        return "It is a prime number" if prime(n) else "It is not a prime number"


num = int(input())
res = check(num)
print(res)