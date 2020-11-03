arr = list(map(int, input().split()))
check = lambda x: False if i % 2 == 0 else True
ls = []
d = {}
s = 0
for i in range(len(arr)):
    s += arr[i]
    if check(s):
        ls.append(arr[0: i + 1])
    if s in d:
        ls.append(ar[d[s] + 1: i + 1])
    else:
        d[s] = i

    print(d)

print(ls)