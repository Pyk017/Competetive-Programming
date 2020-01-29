def recur(n):
    if len(n) == 1:
        return n
    return recur(str(sum(map(int, n))))


def super_digit(num, k):
    return recur(str(int(num) * k))


number = input().split()
result = super_digit(number[0], int(number[1]))
print(result)
