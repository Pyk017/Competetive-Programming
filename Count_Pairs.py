# Count Pairs
# Given an array of integers A, and an integer K find number of happy elements.
# Element X is happy if there exists at least 1 element whose difference is less than K i.e., an element X is happy,
# if there is another element in the range [X-K, X+K] other than X itself.

# Example:
# Input :
# 6 3
# 5 5 7 9 15 2
# Output :
# 5

# Input : 
# 3 2
# 1 3 5
# Output :
# 3



def count_pairs(n, k, ar):
    count = 0
    flag = False
    for i in range(len(ar)):
        left, right = i - 1, i + 1
        while left > 0:
            # print('left :- ', i, left)
            if left > 0 and ar[left] in range(ar[i] - k, ar[i] + k + 1):
                flag = True
                break
            left -= 1

        while right < n:
            # print('right :- ', i, right)
            if right < n and ar[right] in range(ar[i] - k, ar[i] + k + 1):
                flag = True
                break
            right += 1
        # print(flag, ar[i])
        if flag:
            count += 1
        
        flag = False
        
    return count

            

n, k = map(int, input().split())
ar = list(map(int, input().split()))
result = count_pairs(n, k, ar)
print(result)