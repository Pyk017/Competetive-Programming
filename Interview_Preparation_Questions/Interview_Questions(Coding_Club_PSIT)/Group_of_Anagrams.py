"""
Given an array of strings, group anagrams together.
Input : ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
Output : [
    ['eat', 'tea', 'ate']
    ['tan', 'nat']
    ['bat']
]
"""
from collections import Counter


def check_anagram(a, b):
    return Counter(a) == Counter(b)


def group_anagram(ar):
    temp = []
    result = []
    i = 0
    while ar:
        temp.append(ar[i])
        j = i
        while j < len(ar)-1:
            if check_anagram(ar[i], ar[j+1]):
                temp.append(ar[j+1])
                ar.pop(j+1)
            j += 1
        ar.pop(i)
        # print(temp)
        result.append(temp)
        temp = []

    return result


strings = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
new_str = group_anagram(strings)
print('Groups of Anagrams are :- ', new_str)
