def calculate(ar):
    b = [k + 1 for k in range(len(ar))]
    index_dict = {v: u for u, v in enumerate(ar)}
    i, count = 0, 0
    while i < len(ar):
        if ar[i] != b[i]:
            temp = index_dict[b[i]]
            t2 = ar[i]
            ar[i], ar[temp] = ar[temp], ar[i]
            index_dict[t2] = temp
            index_dict[b[i]] = i
            count += 1
        i += 1
    return count

n = int(input())
array = list(map(int, input().split()))
res = calculate(array)
print(res)
 