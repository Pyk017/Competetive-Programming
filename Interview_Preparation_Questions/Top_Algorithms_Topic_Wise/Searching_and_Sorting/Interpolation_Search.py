 def interpolationSearch(arr, lo, hi, x):

    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
 
        # Probing the position with keeping
        # uniform distribution in mind.
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))
 

        if arr[pos] == x:
            return pos
 

        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1,
                                       hi, x)
 
 
        if arr[pos] > x:
            return interpolationSearch(arr, lo,
                                       pos - 1, x)
    return -1
 
arr = list(map(int, input().split()))
n = len(arr)

x = 18
res = interpolationSearch(arr, 0, n - 1, x)
print(res) if res != -1 else print("Element not found!")
