n = int(input())
array = list(map(int, input().split()))
array.sort()
result = min(abs(x - y) for x, y in zip(array, array[1:]))
print(result)
