def spread(ar):
    if len(ar) == 2:
        diff = abs(ar[0] - ar[1])
        return (1, 1) if diff > 2 else (2, 2)
    else:
        res = []
        b, w = 1, 1
        for i in range(1, len(ar)):
            diff = abs(ar[i-1] - ar[i])
            res.append(diff)
        temp = 1
        ls = []
        count = 0
        for j in range(len(res)):
            if res[j] <= 2:
                count += 1
                temp += res[j]
            else:
                ls.append(temp)
                temp = 1
        
        if count == len(res):
            return (len(ar), len(ar))
        else:
            ls.append(temp)
            return (min(ls), max(ls))


n = int(input())
arr = list(map(int, input().split()))
res = spread(arr)
print(res)