def parking(l, b, ar):
    for i in range(l):
        for j in range(b):
            if ar[i][j] == 1:
                break
        if ar[i][j] == 1:
            break

    I, J = i, j
    K, L = I, J
    count = 0 
    d = dict()
    for i in range(I, l):
        
        for j in range(J, b):
            if ar[i][j] == 1:
                temp = abs(K - i) + abs(L - j)
                K = i
                L = j
                if temp != 1:
                    d[temp] = 1
                    
        
    return len(d)      


l = 2
b = 2
ar = [[1, 1],
       [0, 1]]
print(parking(l, b, ar))