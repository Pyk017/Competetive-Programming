import math
import sys

# p = [0]*10000000
# s = [0]*10000000
p = [0]*10
s = [0]*10
n = int(input())
if n == 1:
    print(int(input()) + 1)
    sys.exit()

ls = list(map(int, input().split()))
for i in range(n):
    p[i+1] = math.gcd(ls[i], p[i])

for j in range(n, 0, -1):
    s[j] = math.gcd(s[j+1], ls[j-1])

for k in range(1, n+1):
    print(p[k-1], s[k+1])
    cur = math.gcd(p[k-1], s[k+1])
    if ls[k-1] % cur != 0:
        print(cur)
        sys.exit()
