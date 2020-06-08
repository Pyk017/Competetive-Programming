from collections import Counter

def ana(a, b):
    res = 0
    res += sum((Counter(a) - Counter(b)).values())
    res += sum((Counter(b) - Counter(a)).values())
    return res

str1 = input()
str2 = input()
result = and(str1, str2)
print(result)