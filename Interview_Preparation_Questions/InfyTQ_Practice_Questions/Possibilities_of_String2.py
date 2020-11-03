from itertools import permutations

s = input()
for j in range(len(s)):
    for i in sorted(list(permutations(s, j + 1))):
        print(''.join(i))