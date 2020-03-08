def count_one(num):
    count = 0
    while num:
        num = num & (num - 1)
        count += 1
    return 1 if count % 2 == 0 else 0


for _ in range(int(input())):
    n, q = map(int, input().split())
    ls = list(map(int, input().split()))
    for _ in range(q):
        even, odd = 0, 0
        m = int(input())
        temp = list(map(lambda x: x ^ m, ls))
        for i in temp:
            if count_one(i):
                even += 1
            else:
                odd += 1

        print(even, odd)
