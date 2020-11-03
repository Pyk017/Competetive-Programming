def squaring(n):
    res = 0
    for i in n:
        res += int(i)**2
        
    return True if res % 2 == 0 else False


s = input().split(',')
result = []
for i in s:
    a, n = i.split(':')
    a = list(a)
    if squaring(n):
        a.insert(0, a.pop())
    else:
        a.append(a.pop(0))
        a.append(a.pop(0))
    result.append(''.join(a))
        
print(*result)
