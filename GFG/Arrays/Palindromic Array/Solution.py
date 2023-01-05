def PalinArray(arr, n):
    for x in arr:
        if str(x) == str(x)[::-1]:
            return 0
        
    return 1;


if __name__=="__main__":
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(PalinArray(arr, n))
        