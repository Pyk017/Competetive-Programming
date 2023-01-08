def rotate(arr, n):
    i = n - 1
    temp = arr[i]
    
    while i > 0:
        arr[i] = arr[i - 1]
        i -= 1
        
    arr[0] = temp
    
    
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().strip().split()))
    rotate(a, n)
    print(*a)