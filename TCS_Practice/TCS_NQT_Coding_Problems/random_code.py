# tour = {
#     1: 'Malaysia',
#     2: 'Australia',
#       3:  'Germany',
#        4: 'Dubai',
#         5: 'France'
#     }

# ls = [0 for i in range(5)]

# for i in range(10):
#     rank = int(input())
#     if rank == 1:
#         ls[(i % 5)] += 1


# # print(ls)

# ls = list(enumerate(ls))
# ls.sort(reverse=True, key=lambda x: x[1])
# # print(ls)
# for i in range(5):
#     if ls[i][1] != 0:
#         print(tour[ls[i][0] + 1])


n = int(input())
ls = []
count = 0
while True:
    try:
        ls.append(int(input()))
    except ValueError:
        if len(ls) > n:
            print("INVALID INPUT")
            exit()


print(ls)
