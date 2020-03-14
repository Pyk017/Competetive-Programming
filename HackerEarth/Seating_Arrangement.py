# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/description/

import math as m
for _ in range(int(input())):
    num = int(input())
    ls = [6+7]
    for i in range(10):
        ls.append(ls[i] + 24)
    l, r, temp = 0, 0, 0
    for j in ls:
        l, r = m.floor(j/2), m.ceil(j/2)
        if num > r+5:
            pass
        else:
            temp = j
            break
    res_num = temp - num
    res_alpha = num % 6
    result = str(res_num)
    if res_alpha in [1, 0]:
        result += ' ' + 'WS'
    elif res_alpha in [2, 5]:
        result += ' ' + 'MS'
    else:
        result += ' ' + 'AS'
    print(result)
