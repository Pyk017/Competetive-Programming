def bigger(s):
    for i in reversed(range(len(s) - 1)):
        if s[i] < s[i + 1]:
            for j in reversed(range(i + 1, len(s))):
                if s[i] < s[j]:
                    l = list(s)
                    l[i], l[j] = l[j], l[i]
                    return ''.join(l[:i + 1] + l[i + 1:][::-1])
    return 'no answer'


for _ in range(int(input())):
    string = input()
    res = bigger(string)
    print(res)
