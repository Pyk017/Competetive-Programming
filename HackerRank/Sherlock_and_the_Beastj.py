def decent_number(num):
    if num <= 2:
        return -1
    elif num == 3:
        return '555'
    elif num == 5:
        return '33333'
    else:
        y = num
        while y % 3 != 0:
            y -= 5
        if y < 0:
            return '-1'
        else:
            return y*'5' + (num - y)*'3'


n = int(input())
print(decent_number(n))
