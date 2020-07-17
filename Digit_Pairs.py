def calculate(a):
    f, s, t = int(a[0]), int(a[1]), int(a[2])
    return str(max(f, s, t) * 11 + min(f, s, t) * 7)[-2:]

def calc_bit_score(ar):
    res = list(map(calculate, ar))
    d = dict()
    for i in res:
        if i[0] not in d:
            d[i[0]] = 1
        else:
            d[i[0]] += 1
    
    pairs = 0
    print(res)
    for i, j in d.items():
        if j == 2:
            pairs += 1
        elif j > 2:
            pairs += 2

    return pairs
    

n = int(input())
ar = list(input().split())
result = calc_bit_score(ar)
print(result)