ls = [[] for i in range(100)]
n = int(input())
for i in range(n):
    a, b = input().split()
    if i < n//2:
        b = '-'
    ls[int(a)].append(b)

print(' '.join([element for sublist in ls for element in sublist]))
