<<<<<<< HEAD
"""
Sample Input : 2 4
               16 32 96
Output : 3
Explanation : 2 and 4 divide evenly into 4, 8, 12, and 16.
4, 8 and 16 divide evenly into 16, 32, 96.
4, 8 and 16 are the only 3 numbers for which each elements of 'a' is a factor and each is a factor of all elements of b.
"""


def get_total(a, b):
    ls, count = [], 0
    for i in range(max(a), min(b)+1):
        count = 0
        for j in a:
            if i % j == 0:
                count += 1

        if count == len(a):
            ls.append(i)

    count, result = 0, []
    for i in ls:
        count = 0
        for j in b:
            if j % i == 0:
                count += 1

        if count == len(b):
            result.append(i)

    print(result)
    return len(result)


arr1 = [2, 6]
arr2 = [24, 36]
print(get_total(arr1, arr2))
=======
"""
Sample Input : 2 4
               16 32 96
Output : 3
Explanation : 2 and 4 divide evenly into 4, 8, 12, and 16.
4, 8 and 16 divide evenly into 16, 32, 96.
4, 8 and 16 are the only 3 numbers for which each elements of 'a' is a factor and each is a factor of all elements of b.
"""


def get_total(a, b):
    ls, count = [], 0
    for i in range(max(a), min(b)+1):
        count = 0
        for j in a:
            if i % j == 0:
                count += 1

        if count == len(a):
            ls.append(i)

    count, result = 0, []
    for i in ls:
        count = 0
        for j in b:
            if j % i == 0:
                count += 1

        if count == len(b):
            result.append(i)

    print(result)
    return len(result)


arr1 = [2, 6]
arr2 = [24, 36]
print(get_total(arr1, arr2))
>>>>>>> competetive committed
