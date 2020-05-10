def spread(ar):
    mini, maxi = 11, -1
    
    if len(ar) == 2:
        return (1, 1)
    
    total = 1
    for i in range(1, len(ar)):
        if abs(ar[i-1] - ar[i]) <= 2:
            total += 1
        else:
            mini = min(mini, total)
            maxi = max(maxi, total)
            total = 1

    mini = min(mini, total)
    maxi = max(maxi, total)
    
    if maxi == len(ar):
        mini = maxi
    
    return (mini, maxi)


n = int(input())
arr = list(map(int, input().split()))
res = spread(arr)
print(*res)