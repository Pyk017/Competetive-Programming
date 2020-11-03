def majority(a):
    d = {}
    test = len(a) // 2
    res = False
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
            if d[i] > test:
                res = str(i)
    
    return res if res else '-1'
    
for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    print(majority(ar))