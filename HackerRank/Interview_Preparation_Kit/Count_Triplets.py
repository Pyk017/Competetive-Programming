from collections import Counter

def triplets(ar, r):
    left_map = Counter()
    right_map = Counter(ar)
    count = 0
    for j in ar:
        try:
            right_map[j] -= 1
            i = left_map[j / r]
            k = right_map[j * r]
            count += i * k
            left_map[j] += 1
        except:
            pass
        
    return count

n, r = map(int, input().split())
arr = list(map(int, input().split()))
res = triplets(ar, r)
print(res)
