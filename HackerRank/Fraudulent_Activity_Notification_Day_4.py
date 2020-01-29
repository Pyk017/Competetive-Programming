<<<<<<< HEAD
from bisect import bisect_left, insort_left


def get_median(a):
    if len(a) % 2 != 0:
        return a[len(a) // 2]
    else:
        c = (a[(len(a) // 2) - 1] + a[(len(a) // 2)]) / 2
        return c


def act(a, x):
    notify, i = 0, 0
    temp = sorted(a[i:x])
    for j in range(x, len(a)):
        res = get_median(temp)
        if a[j] >= 2 * res:
            notify += 1
        i += 1
        del temp[bisect_left(temp, a[j - x])]
        insort_left(temp, a[j])

    return notify


n, m = list(map(int, input().split()))
ls = list(map(int, input().split()))
result = act(ls, m)
print(result)
=======
from bisect import bisect_left, insort_left


def get_median(a):
    if len(a) % 2 != 0:
        return a[len(a) // 2]
    else:
        c = (a[(len(a) // 2) - 1] + a[(len(a) // 2)]) / 2
        return c


def act(a, x):
    notify, i = 0, 0
    temp = sorted(a[i:x])
    for j in range(x, len(a)):
        res = get_median(temp)
        if a[j] >= 2 * res:
            notify += 1
        i += 1
        del temp[bisect_left(temp, a[j - x])]
        insort_left(temp, a[j])

    return notify


n, m = list(map(int, input().split()))
ls = list(map(int, input().split()))
result = act(ls, m)
print(result)
>>>>>>> competetive committed
