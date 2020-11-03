from collections import Counter

for _ in range(int(input())):
    string1 = input()
    string2 = input()
    res = 0
    res += sum((Counter(string1) - Counter(string2)).values())
    res += sum((Counter(string2) - Counter(string1)).values())
    print(res)

