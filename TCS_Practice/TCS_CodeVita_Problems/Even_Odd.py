low, high = map(int, input().split())
k = int(input())
total_element = high - low + 1
result = ((total_element**k) // 2) % 10000000007
print(result, end='')
