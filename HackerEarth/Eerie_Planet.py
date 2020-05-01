H, P, Q = map(int, input().split())
d = list()
for _ in range(P):
    height, start, end = map(int, input().split())
    d.append((height, start, end))
max_height = max(d, key=lambda x: x[0])[0]
for _ in range(Q):
    h, time = map(int, input().split())
    if h > max_height:
        print("YES")
    else:
        flag = True
        for i in d:
            if i[1] <= time <= i[2] and i[0] >= h:
                print("NO")
                flag = False
                break
        if flag:
            print("YES")