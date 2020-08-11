def lds(ar, n):
    temp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if ar[i] < ar[j] and temp[i] < temp[j] + 1:
                temp[i] = temp[j] + 1

    return max(temp)


n = int(input())
ar = list(map(int, input().split()))
print(lds(ar, n))