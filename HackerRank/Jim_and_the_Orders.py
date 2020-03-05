t = int(input())
ls = []
customer = 1
for _ in range(t):
    order, prep = map(int, input().split())
    ls.append((customer, order+prep))
    customer += 1
ls.sort(key=lambda x: x[1])
res = ' '.join(list(map(lambda x: str(x[0]), ls)))
print(res)
