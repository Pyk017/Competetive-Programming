def gameOfThrones(s):
    d = {i: 0 for i in string.ascii_lowercase}
    for j in s:
        d[j] += 1
    odd, even = 0, 0
    for k, v in d.items():
        if v != 0:
            if v % 2 == 0:
                even += 1
            else:
                odd += 1
    
    if len(s) % 2 == 0 and odd == 0:
        return 'YES'
    elif len(s) % 2 != 0 and odd == 1:
        return 'YES'
    return 'NO'


st = input()
res = gameOfThrones(st)
print(res)
