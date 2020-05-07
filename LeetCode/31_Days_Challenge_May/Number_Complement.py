def find_complement(num):
    n = num
    flip = lambda x: '1' if x == '0' else '0'
    m = list(map(flip, bin(n)[2:]))
    rs = int(''.join(m), 2)
    return rs

n = int(input())
print(find_complement(n))