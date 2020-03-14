# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/
n = int(input())
arr = list(map(int, input().split()))
product = 1
for i in arr:
    product = (product * i) % (10**9 + 7)
print(product)
