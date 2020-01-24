def msb(x):
    ret = 0
    while ((x >> (ret + 1)) != 0):
        ret = ret + 1
    return ret


def xorRange(l, r):
    max_bit = msb(r)
    mul = 2
    ans = 0
    for i in range(1, max_bit + 1):
        if ((l // mul) * mul == (r // mul) * mul):
            if ((((l & (1 << i)) != 0) and
                 (r - l + 1) % 2 == 1)):
                ans = ans + mul
            mul = mul * 2
            continue

        odd_c = 0

        if (((l & (1 << i)) != 0) and l % 2 == 1):
            odd_c = (odd_c ^ 1)

        if (((r & (1 << i)) != 0) and r % 2 == 0):
            odd_c = (odd_c ^ 1)

        if (odd_c):
            ans = ans + mul

        mul = mul * 2

    zero_bit_cnt = (r - l + 1) // 2

    if ((l % 2 == 1) and (r % 2 == 1)):
        zero_bit_cnt = zero_bit_cnt + 1

    if (zero_bit_cnt % 2 == 1):
        ans = ans + 1

    return ans


for _ in range(int(input())):
    L, R = map(int, input().split())
    print(xorRange(L, R))
