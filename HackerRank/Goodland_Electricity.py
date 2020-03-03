def good_land(n, k, city):
    i, j, loc, count, flag = 0, 0, 0, 0, False
    while i < len(city):
        count += 1
        j = i + k - 1
        if j > n:
            j = n - 1
        while loc <= j < n and city[j] == 0:
            j -= 1
        if j < loc:
            return -1
        else:
            loc = j + 1
            j += k
            i = j

    return count


(N, K) = map(int, input().split())
cities = list(map(int, input().split()))
print(good_land(N, K, cities))
