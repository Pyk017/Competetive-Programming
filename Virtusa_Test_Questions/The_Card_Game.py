def longest_min_Subarray(arr):
    current_min = arr[0]
    global_min = arr[0]
    for i in range(1, len(arr)):
        current_min = min(current_min, current_min + arr[i])
        global_min = min(current_min, global_min)

    return global_min

def card(input1):
    ans = longest_min_Subarray(input1) * (-1)
    ans = 2 * ans + sum(input1)
    return ans

inp_arr = list(map(int, input().split()))
result = card(inp_arr)
print(result)
