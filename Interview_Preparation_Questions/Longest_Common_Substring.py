def lcs(X, Y):
    ls = [[0 for _ in range(len(Y) + 1)] for _ in range(len(X) + 1)]
    result = 0
    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            if X[i - 1] == Y[j - 1]:
                ls[i][j] = ls[i - 1][j - 1] + 1
                result = max(result, ls[i][j])
            else:
                ls[i][j] = 0
                
    return result
    
for _ in range(int(input())):
    n, m = map(int, input().split())
    str1 = input()
    str2 = input()
    print(lcs(str1, str2))