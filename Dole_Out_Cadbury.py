def calculate(length, width):
    count = 0
    
    if length == width:
        return 1
    
    while length != 1 and width != 1:
        if length == width:
            return count + 1
        count += 1
        if length < width:
            width = width - length
        else:
            length = length - width

    return width + count if length == 1 else length + count
    


def cadbury(maxl, minl, maxw, minw):
    res = 0
    for i in range(minl, maxl + 1):
        for j in range(minw, maxw + 1):
            res += calculate(i, j)
            # print(i, j)
            # print(calculate(i, j))

    print(res)

minl, maxl, minw, maxw = list(map(int, input().split()))
result = cadbury(maxl, minl, maxw, minw)
print(result)