def printFirstNegativeInteger( A, N, K):
    queue = []
    res = []
    
    for i in range(K):
        if A[i] < 0:
            queue.append(A[i])
            
    if len(queue) > 0:
        res.append(queue[0])
    else:
        res.append(0)
        
        
    for i in range(K, N):
        ins = A[i]
        rem = A[i - K]
        
        if ins < 0:
            queue.append(ins)
            
        if rem in queue and rem == queue[0]:
            queue.pop(0)
            
        if len(queue) > 0:
            res.append(queue[0])
        else:
            res.append(0)
            
    return res


def main():
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    k = int(input())
    
    answer = printFirstNegativeInteger(a, n, k)
    for i in answer:
        print(i,end=" ")
    print()
