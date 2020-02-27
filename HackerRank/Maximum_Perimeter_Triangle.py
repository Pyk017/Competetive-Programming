def maximum_perimeter_triangle(array):
    array.sort()
    maxi = 0
    res = []
    for i in range(len(array)-2):
        if array[i] + array[i+1] <= array[i+2]:
            pass
        else:
            sumi = array[i] + array[i+1] + array[i+2]
            if sumi > maxi:
                res = [array[i], array[i+1], array[i+2]]
                maxi = sumi

    return res if maxi != 0 else [-1]


n = int(input())
input_string = list(map(int, input().split()))
print(maximum_perimeter_triangle(input_string))
