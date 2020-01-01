from itertools import combinations, permutations
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    cmb = min(list(map(sum, list(permutations(l, k)))))
    print (cmb)
