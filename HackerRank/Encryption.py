import math

string = ''.join(input().split())
n = math.sqrt(len(string))
row, col = math.floor(n), math.ceil(n)
if (row * col) < len(string):
    row += 1
ls = []
start = 0
for i in range(row):
    ls.append(string[start: start + col])
    start += col

res = ''
for i in range(len(ls[0])):
    for j in range(len(ls)):
        try:
            res += ls[j][i]
        except:
            pass

    res += ' '

print(res)


#   or
"""
    c = math.ceil(math.sqrt(len(s)))
    return ' '.join(map(lambda x: s[x::c], range(c)))
    
    where s is the input string.
"""