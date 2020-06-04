Fails TestCase 11.

"""   
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
"""

Passes All TestCases.

def energy(arr):
    e = 0
    for i in range(len(arr) - 1, -1, -1):
        e = (e + arr[i] + 1) // 2
    return e


n = int(input())
input_list = list(map(int, input().split()))
print(energy(input_list))
