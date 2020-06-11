from collections import Counter

string = input()
d = dict(Counter(string))
v = dict(Counter(d.values()))
n = len(v)

if n == 1:
    print("YES")

elif n == 2 and 1 in v.values():
    K = list(v.keys())
    if v.get(1, 0) == 1 or abs(K[0] - K[1]) == 1:
        print("YES")
    else:
        print("NO")

else:
    print("NO")

