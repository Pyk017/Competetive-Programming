d1 = {12: 25, 3: 50, 6: 75, 9: 100}
ls = []
for _ in range(int(input())):
    d2 = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for __ in range(int(input())):
        m, n = input().split()
        no = int(n)
        d2[m] += d1[no]
    ans = 0
    print(d2)
    for i, j in d2.items():
        if j != 0:
            ans += j
        else:
            ans -= 100

    ls.append(ans)

print(ls)
print(sum(ls))
