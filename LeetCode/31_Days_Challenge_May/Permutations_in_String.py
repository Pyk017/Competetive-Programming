import string
from itertools import permutations
def check_inclusion(a, b):
    d1 = {i: 0 for i in string.ascii_lowercase}
    d2 = {i: 0 for i in string.ascii_lowercase}
    for i in a:
        d1[i] += 1
    for j in b:
        d2[j] += 1

    temp = ''
    for i in a:
        if d2[i] > 0:
            temp += i
    if temp == '':
        return False
    print(temp)
    for j in permutations(temp, len(temp)):
        print(j)
        if ''.join(j) in b:
            return True

    return False
    

    



s1 = input()
s2 = input()
res = check_inclusion(s1, s2)
print(res)