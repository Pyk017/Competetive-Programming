def mincost(input1, input2):
    temp = -1
    mini = 99999
    total = 0
    for i in  input1:
        for j in range(len(i)):
            if i[j] < mini and j != temp:
                mini = i[j]
                temp = j
        
        total += mini
        mini = 99999

    return total


# arr = [[1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12]]
# student = 3

arr = [[14, 16, 10, 12],
        [8, 5, 6, 1]]
student = 2
print(mincost(arr, student))