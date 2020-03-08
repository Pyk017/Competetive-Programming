import sys
for _ in range(int(input())):
    n, m = map(int, input().split())
    F = list(map(int, input().split()))
    P = list(map(int, input().split()))
    temp = [0]*(m+1)
    for i in range(n):
        temp[F[i]] += P[i]
    # print(temp)
    flag = False
    mini = sys.maxsize
    for i in temp:
        if i != 0 and i < mini:
            mini = i
            flag = True

    print(mini) if flag else print(0)
