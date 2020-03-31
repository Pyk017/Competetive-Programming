n, q = map(int, input().split())
seq_list = [[] for _ in range(n)]
last_ans = 0
for _ in range(q):
    opt, x, y = map(int, input().split())
    ind = (x ^ last_ans) % n
    if opt == 1:
        seq_list[ind].append(y)
    elif opt == 2:
        last_ans = seq_list[ind][y % len(seq_list[ind])]
        print(last_ans)
