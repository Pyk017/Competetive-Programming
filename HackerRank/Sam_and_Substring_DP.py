mod = 10000007


def substring(n):
    a, b = [1]*len(n), [1]*len(n)
    for i in range(1, len(n)):
        a[i] = (10 * a[i - 1]) % mod
        b[i] = (b[i - 1] + a[i]) % mod

    result = 0
    for i in range(len(n)):
        result += (int(n[i]) * b[len(n) - i - 1] * (i + 1)) % mod

    return result


num = input()
print(substring(num))
