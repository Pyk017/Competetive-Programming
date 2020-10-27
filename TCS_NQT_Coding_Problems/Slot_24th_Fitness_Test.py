res = []
maxi = -1

for i in range(3):
    a = int(input())
    b = int(input())
    c = int(input())
    avg = round((a + b + c) / 3)
    if int(avg) >= 70 and avg >= maxi:
        res.append((avg, i + 1))
        maxi = avg

for i, j in res:
    print("Trainee Number : {}".format(j))


