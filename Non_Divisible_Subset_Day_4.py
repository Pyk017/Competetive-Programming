"""
Sample Input : 1 7 2 4
Output : 3
Explanation : The sums of all permutations of two elements from S = {1, 7, 2, 4} are:
1 + 7 = 8
1 + 2 = 3
1 + 4 = 5
7 + 2 = 9
7 + 4 = 11
2 + 4 = 6
We see that only S' = {1, 7, 4} will not ever sum to a multiple of k = 3
"""


def non_divisible_set(s, tar):
    a = [0 for i in range(tar)]
    for i in s:
        a[i % tar] += 1
    m = 1 if a[0] > 0 else 1
    for i in range(1, tar//2 + 1):
        if i != tar-i:
            m += max(a[i], a[k-i])
        else:
            m += 1

    return m


array = list(map(int, input('Enter elements in the list :- ').split()))
k = int(input('Enter target element :- '))
print(non_divisible_set(array, k))
