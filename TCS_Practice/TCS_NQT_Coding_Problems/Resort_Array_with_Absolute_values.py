def merge(ls):
    n = len(ls)
    neg = [ (-1) * i for i in ls if i < 0][::-1]
    pos = [i for i in ls if i >= 0]
    i, j = 0, 0
    res = []
    while(i < len(neg) and j < len(pos)):
        if neg[i] <= pos[j]:
            res.append(neg[i])
            i += 1
        else:
            res.append(pos[j])
            j += 1
        
    while i < len(neg):
        res.append(neg[i])
        i += 1

    while j < len(pos):
        res.append(pos[j])
        j += 1
    
    return res


ls = list(map(int, input().split()))
new_ls = merge(ls)
print(new_ls)
