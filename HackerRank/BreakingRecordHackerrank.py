def breakingRecords(score):
    min = max = score[0]
    count, count2 = 0,0
    for i in range(1,len(score)):
        if score[i] > max:
            max = score[i]
            count += 1
        if score[i] < min:
            min = score[i]
            count2 += 1

    l = [count,count2]
    return l


n = int(input())
scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)
print(result)