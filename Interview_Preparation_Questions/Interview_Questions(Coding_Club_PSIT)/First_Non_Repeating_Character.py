# Given a string find the first non-repeating character in it and return its index. If it does  not exists, return -1.
# Input: a = 'codingclubindia'
# Output : 1, o
from collections import Counter


def find_character(s):
    ls = dict(Counter(s))
    ls = sorted(ls.items(), key=lambda x: (x[1], x[0]))
    if ls[0][1] == 1:
        print("First Non-repeating Character is :- ", ls[0][0])
        return s.index(ls[0][0])
    return -1


string = input('Enter a String :- ')
print("Non Repeating Character is at index position :- ", find_character(string))
