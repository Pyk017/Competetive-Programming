def find(arr, n, x):
    if x in arr:
        return [arr.index(x), n - arr.index(x) - 1]
    return [-1, -1]


if __name__ == "__main__":
    line = list(map(int, input().strip().split()))
    n = line[0]
    x = line[0]
    arr = list(map(int, input().strip().split()))
    ans = find(arr, n, x)
    print(*ans)
