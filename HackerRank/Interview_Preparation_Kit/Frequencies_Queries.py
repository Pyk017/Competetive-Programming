
from collections import Counter

# def freqQuery(queries):   # TestCase 11 failed timeout 
#     d1 = Counter()
#     res = []
#     for op, num in queries:
#         if op == 1:
#             d1[num] += 1

#         elif op == 2:
#             if d1[num] > 0:
#                 d1[num] -= 1
#             else:
#                 del d1[num]

#         elif op == 3:
#             if num in set(d1.values()):
#                 res.append(1)
#             else:
#                 res.append(0)

#     return res

def freqQuery(queries):
    freq = Counter()
    cnt = Counter()
    result = []
    for op, num in queries:
        if op == 1:
            cnt[freq[num]] -= 1
            freq[num] += 1
            cnt[freq[num]] += 1

        elif op == 2:
            if freq[num] > 0:
                cnt[freq[num]] -= 1
                freq[num] -= 1
                cnt[freq[num]] += 1

        else:
            if cnt[num] > 0:
                result.append(1)
            else:
                result.append(0)

    return result


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = freqQuery(arr)
print('\n'.join(res))
