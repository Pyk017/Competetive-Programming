"""
Input :
5 2
1 5 3 4 2

Output :
3

Explanation :
As there are 3 pair {[1, 3], [5, 3], [4, 2]} the difference of all pairs are equals to 2.
"""


def pairs(a, target):
    i, j, count = 0, 1, 0
    a.sort()
    while j < n:
        diff = abs(a[i] - a[j])
        if diff == target:
            count += 1
            j += 1
        elif diff > target:
            i += 1
        else:
            j += 1

    return count


n, k = list(map(int, input().split()))
ls = list(map(int, input().split()))
print(pairs(ls, k))
