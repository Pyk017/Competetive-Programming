def sorting(a, n):
    count = 0
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1
    
    print('Array is sorted in {} swaps.'.format(count))
    print('First Element:', a[0])
    print('Last Element:', a[-1])


n = int(input())
ar = list(map(int, input().split()))
sorting(ar, n)