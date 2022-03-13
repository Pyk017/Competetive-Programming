def solution(a, b, x, y):
    count = 0

    while a > x and b > y:
        a -= x
        b -= y
        count += 1

    print(a, b)

    return count

a, b = list(map(int, input().split()))
x, y = 1, 2
result = solution(a, b, x, y)
x, y = y, x
result += solution(a, b , x, y) 
print(result)
