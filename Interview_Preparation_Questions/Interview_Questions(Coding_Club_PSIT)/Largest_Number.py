from itertools import permutations
import operator


def largest(l):
    lis = []
    for i in permutations(l, len(l)):
        lis.append(int(''.join(list(map(str, i)))))

    return max(lis)


list1 = list(map(int, input("Enter array :- ").split()))
list1 = sorted(list1, key=abs)
print(list1)
print("Largest Number is :- ", largest(list1))
