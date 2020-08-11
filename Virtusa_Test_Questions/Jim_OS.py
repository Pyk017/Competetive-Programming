def scheduling(input1, input2, input3):
    # input1 = 5
    # input2 = [0, 3, 9, 2, 6]
    # input3 = [3, 4, 2, 9, 6]    
    ls = list(zip(input2, input3))
    ls = sorted(ls, key= lambda x: x[0])
    res = ls[0][0] + ls[0][1]
    for i in range(1, len(ls)):
        res += ls[i][1] 
    return res

# n = 5
# A = [0, 3, 9, 2, 6]
# B = [3, 4, 2, 9, 6]
n = 1
A = [2]
B = [8]
print(scheduling(n, A, B))