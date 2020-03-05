for _ in range(int(input())):
    n, k = map(int, input().split())
    array_a = list(map(int, input().split()))
    array_b = list(map(int, input().split()))
    array_a.sort()
    array_b.sort(reverse=True)
    flag = False
    for i in range(n):
        if array_a[i] + array_b[i] >= k:
            flag = True
        else:
            flag = False
            break
    print('YES') if flag else print("NO")
