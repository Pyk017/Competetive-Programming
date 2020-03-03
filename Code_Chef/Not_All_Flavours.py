import collections as c

t = int(input())
for _ in range(t):
    (N, K) = map(int, input().split())
    array = list(map(int, input().split()))
    if len(set(array)) == K-1:
        print(N)
    else:
        array_string = ''.join(list(map(str, array)))
        counting = dict(c.Counter(array))
        minimum = list(sorted(counting.items(), key=lambda x: (x[1], x[0])))[0][0]
        new_list = array_string.split(str(minimum))
        maxi = 0
        for i in new_list:
            if len(i) > maxi:
                maxi = len(i)
        print(maxi)
