a = [[2, 4, 6, 8],
     [1, 3, 5, 7],
     [8, 6, 4, 2],
     [7, 5, 3, 1]]
     
     
     
for i in range(len(a)):
    for j in range(len(a)//2):
        a[i][j], a[i][len(a) - 1 - j] = a[i][len(a) - 1 - j], a[i][j]
        
print(a)