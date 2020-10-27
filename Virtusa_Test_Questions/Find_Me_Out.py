def find_me_out(input1):
    n = 2
    while n <= 10000:
        sumi = sum(list(map(int, str(n))))
        if n % input1 == 0 and sumi == input1 and n != input1:
            return n
        n += 1

    return -1


n = int(input())
res = find_me_out(n)
print(res)