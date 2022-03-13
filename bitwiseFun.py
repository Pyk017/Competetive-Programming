def Fun(A, B):
    return A + B - 2 * (A & B)


def solution(arr):
    count = 0
    n = len(arr)
    arr.sort()
    res = []
    
    for i in range(n- 2):
        for j in range(i + 1, n - 1): 
            res.append(Fun(arr[i], arr[j]))
            print(arr[i], arr[j])
    
    print(res)
    for i in res:
        for k in range(2, n):
            print(i, arr[k])
            count += Fun(i, arr[k])
            
    return count



n = int(input())
ar = [int(input()) for i in range(n)]
result = solution(ar)
print(result)
