import sys
def kadane(a):
    max_current, max_global = -sys.maxsize, -sys.maxsize
    for i in range(len(a)):
        max_current = max(max_current + a[i], a[i])
        max_global = max(max_current, max_global)
    return max_global

def max_circular_sum(a):
    max_kadane = kadane(a)
    max_wrap = 0
    # print(max_kadane)
    for i in range(len(a)):
        max_wrap += a[i]
        a[i] = -a[i]
    print(kadane(a), max_wrap)
    max_wrap += kadane(a)
    # print(kadane(a))
    return max_wrap if max_wrap > max_kadane else max_kadane


arr = list(map(int, input().split()))
res = max_circular_sum(arr)
print(res)
