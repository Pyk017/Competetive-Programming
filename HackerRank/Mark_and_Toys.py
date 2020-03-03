def mark(toy, k):
    toy.sort()
    sumation = 0
    count = 0
    for i in range(len(toy)):
        if sumation < k:
            sumation += toy[i]
            count += 1
        else:
            break

    # print(sumation)
    return count-1


(N, K) = map(int, input().split())
toys = list(map(int, input().split()))
print(mark(toys, K))
