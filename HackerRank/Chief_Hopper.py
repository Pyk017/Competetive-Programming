import math as m


def energy(arr):
    s, p = 0, 2.0
    for i in range(len(arr)):
        s += arr[i] / p
        p *= 2

    temp = int(m.ceil(s))
    start = temp
    for i in arr:
        start = 2 * start - 1
        if start < 0:
            temp += 1
            break

    return temp


n = int(input())
input_list = list(map(int, input().split()))
print(energy(input_list))
