<<<<<<< HEAD
"""
Sample Input :
2
5
1 1 1 2 2
5
2 1 3 1 2
Output :
0
4
"""
import bisect


def insertion_sort(a):
    b = sorted(a)
    count, p = 0, 0
    for k in a:
        p = bisect.bisect_left(b, k)
        count += p
        b.pop(p)

    return count


for i in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    print(insertion_sort(ls))
=======
"""
Sample Input :
2
5
1 1 1 2 2
5
2 1 3 1 2
Output :
0
4
"""
import bisect


def insertion_sort(a):
    b = sorted(a)
    count, p = 0, 0
    for k in a:
        p = bisect.bisect_left(b, k)
        count += p
        b.pop(p)

    return count


for i in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    print(insertion_sort(ls))
>>>>>>> competetive committed
