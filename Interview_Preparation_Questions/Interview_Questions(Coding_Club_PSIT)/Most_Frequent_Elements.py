"""
Given a non-empty array of integers, return the k most frequent elements.
Input = [1, 1, 1, 2, 2, 3],  k = 2
Output = [1, 2]

Input = [1], k = 1
Output = [1]
"""


from collections import Counter


def frequent(ar, k):
    ls = sorted(dict(Counter(ar)).items(), key=lambda x: (x[1], x[0]), reverse=True)
    ls1 = []
    for i in range(k):
        ls1.append(ls[i][0])

    return ls1


arr = list(map(int, input("Enter elements in the Array :- ").split()))
k = int(input("Enter number of elements :- "))
print("Most Frequent Elements are :- ", frequent(arr, k))
