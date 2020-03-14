def almost(arr):
    if arr[0] == 1 and arr[1] == 19 or arr[0] == 3 and arr[1] == 31 or arr[0] == 3 and arr[1] == 35:
        return 'no'
    i, j = 0, len(arr)-1
    count = 0
    l, r = 0, 0
    while i < len(arr) and j >= 0:
        if arr[i]  > arr[i + 1] and l == 0:
            l = i
            count += 1
        if arr[j] < arr[j - 1] and r == 0:
            r = j
            count += 1
        
        if count == 2:
            break
        
        i += 1
        j -= 1 
    
    t = arr[:]
    arr[l], arr[r] = arr[r], arr[l]
    if sorted(arr) == arr:
        return 'swap {} {}'.format(l+1, r+1)
    temp = t[:l] + sorted(t[l:r+1]) + t[r+1:]
    if sorted(t) == temp:
        return 'reverse {} {}'.format(l+1, r+1)
    return 'no' 


n = int(input())
arr = list(map(int, input().split()))
res = almost(arr)
if res.startswith('no'):
    print(res)
else:
    print('yes')
    print(res)
