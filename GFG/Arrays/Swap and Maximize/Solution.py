def maxSum(arr, n):
    i, j = 0, n - 1
    arr.sort()

    result = 0

    flag = True

    while i < j:
        if flag:
            result += abs(arr[i] - arr[j])
            i += 1
        else:
            result += abs(arr[i] - arr[j])
            j -= 1

    result += abs(arr[i] - arr[j])

    return result


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = maxSum(arr, n)
    print(*ans)
