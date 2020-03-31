from collections import Counter

def sherlock(s):
    count = 0
    for i in range(1, len(s) + 1):
        a = [''.join(list(sorted(s[j: j + i]))) for j in range(len(s) - i + 1)]
        b = Counter(a)
        print(a, b)
        for j in b:
            count += b[j] * (b[j] - 1) // 2
    print(count)


for _ in range(int(input())):
    string = input()
    sherlock(string)
