from collections import Counter

def ransom(magazine, note):
    d_note = dict(Counter(note))
    d_maga = dict(Counter(magazine))
    for i in note:
        if i not in magazine or d_note[i] > d_maga[i]:
            return 'No'
    return 'Yes'


m, n = map(int, input().split())
magazine = input().split()
note = input().split()
res = ransom(magazine, note)
print(res)

# d = dict()
# for i in note:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1

# for j in magazine:
#     if j in d:
#         d[j] -= 1

# flag = False
# for i, j in d.items():
#     if j > 0:
#         print('No')
#         flag = True
#         break

# if not flag:
#     print('Yes')
