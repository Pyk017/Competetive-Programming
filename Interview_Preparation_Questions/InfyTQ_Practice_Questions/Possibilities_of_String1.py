from itertools import permutations

s = input()
ls = sorted(list(permutations(s, len(s))))
for i in ls:
    print(''.join(i))