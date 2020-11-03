arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
       
# Step 1 : Transposing the Matrix

for i in range(len(arr)):
    for j in range(i, len(arr)):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

# Step 2: Mirror Imaging the Matrix

for i in range(len(arr)):
    for j in range(len(arr)//2):
        arr[i][j], arr[i][len(arr) - 1 - j] = arr[i][len(arr) - 1 - j], arr[i][j]
        
print(arr)