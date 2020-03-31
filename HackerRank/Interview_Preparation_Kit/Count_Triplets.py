from collections import Counter

def triplets(ar, r):
    d = dict(Counter(ar))
    result = 0
    for i in ar:
        a1, a2, a3 = i, i * r, i * r * r
        if a2 in d and a3 in d:
            if d[a2] >= d[a3]:
                result += d[a2]
            else:
                result += d[a3]
    return result


n, r = map(int, input().split())
array = list(map(int, input().split()))
res = triplets(array, r)
print(res)
