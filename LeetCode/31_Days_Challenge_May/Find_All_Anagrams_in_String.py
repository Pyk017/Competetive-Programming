from collections import Counter

count = lambda x, y: True if Counter(x) == Counter(y) else False
# Method 1 (Hash Table)
def all_anagram(s, p):
    l = []
    for i in range(len(s)- len(p) + 1):
        if count(s[i: i + len(p)], p):
            l.append(i)
        # print(s[i: i + len(p)], i)

    return l
# Method 1 (Hash Table Modified)
def find_anagram(s, p):
    cnt_p = Counter(p)
    l = []
    for i in range(len(s) - len(p) + 1):
        if cnt_p == Counter(s[i: i + len(p)]):
            l.append(i)

    return i

# Method 2 (Sliding Window Technique)
def all_anagrams(s, p):
    cnt_p = Counter(p)
    n, m = len(s), len(p)
    l = []
    for i in range(n - m + 1):
        if i == 0:
            cnt_s = Counter(s[:m])
        else:
            prev = s[i - 1]
            current = s[i + m - 1]
            cnt_s[prev] -= 1
            cnt_s[current] += 1
            if cnt_s[prev] == 0:
                del cnt_s[prev]
        if cnt_s == cnt_p:
            l.append(i)

    return l


s = input()
p = input()
res = all_anagrams(s, p)
print(res)