"""
Write a program to print all permutations of a given string.
Input : ABC
Output : ABC ACB BAC BCA CBA CAB
"""


def permute(arr, l, r):
    if l == r:
        print(''.join(arr))

    else:
        for i in range(l, r+1):
            arr[i], arr[l] = arr[l], arr[i]
            permute(arr, l + 1, r)
            arr[i], arr[l] = arr[l], arr[i]


string = list(map(str, input("Enter String :- ")))
permute(string, 0, len(string)-1)
