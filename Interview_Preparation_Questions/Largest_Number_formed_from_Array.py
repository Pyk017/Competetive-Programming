for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ar = sorted(ar, key=lambda x: str(x)*10, reverse=True)
    print(''.join([str(i) for i in ar]))
