import collections
stones = input("Enter Stones :- ")
jewel = input("Enter Jewels :- ")
c = dict(collections.Counter(jewel))
sumation = 0
for i in stones:
    if i in c:
        sumation += c[i]

print(sumation)