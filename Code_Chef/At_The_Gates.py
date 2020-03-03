t = int(input())
for _ in range(t):
    (N, K) = map(int, input().split())
    array = input().split()
    while K:
        temp = array.pop()
        if temp in 'H':
            for i in range(len(array)):
                if array[i] == 'H':
                    array[i] = 'T'
                else:
                    array[i] = 'H'
        K -= 1

    result = array.count('H')
    print(result)
