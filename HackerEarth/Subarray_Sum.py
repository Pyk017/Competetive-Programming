import sys
def calculate(a):
    ls = [i - 1 for i in a]
    # print(ls)
    s = 0
    for i in range(len(ls)):
        if ls[i] > 0:
            s += ls[i]
            ls[i] = s
        else:
            if s < 0:
                s += ls[i]
                ls[i] = s
            else:
                s = ls[i]
    return min(ls)


for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    res = calculate(ar)
    print(res)
