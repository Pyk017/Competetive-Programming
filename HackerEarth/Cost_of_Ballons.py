# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/mojtaba-prepares-contest-29b2a044/
for _ in range(int(input())):
    green, purple = map(int, input().split())
    n = int(input())
    result = 0
    _a, _b = 0, 0
    for i in range(n):
        a, b = map(int, input().split())
        _a += a
        _b += b
    result = min(_a*green + _b*purple, _a*purple + _b*green)
    print(result)
