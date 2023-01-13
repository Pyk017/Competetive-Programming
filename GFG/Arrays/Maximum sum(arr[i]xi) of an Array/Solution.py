def Maximize(a, n):
    a.sort()
    result = 0

    for i in range(n):
        result += a[i] * i

    return result % 1000000007


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().strip().split()))
    result = Maximize(arr, n)
    print(result)
