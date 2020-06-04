'''
The idea is to make it in two steps. 1 - Run through the half of list, 
increment those elements which are not equal (arr[i] != arr[n - 1 - i]) and marked indices. 
Every match decrements k. In this circle also check out if k < 0 then it's impossible to make it a palindrome. 
2 step - run through it again and check similar elements. 
If it is not equal to 9 - make them 9, decrement k - if index is in marked indices - by 1 otherwise by 2.
'''


def highestValuePalindrome(s, n, k):
    if n == 1:
        if k == 1:
            return '9'
        else:
            return '-1'
    arr = list(s)
    changes = [0 for _ in range(n)]
    for i in range((n // 2) + (n & 1)):
        if arr[i] != arr[n - i - 1]:
            arr[i] = arr[n - i - 1] = max(arr[i], arr[n - i - 1])
            changes[i] += 1
            k -= 1
        if k < 0:
            return '-1'

    for i in range((n // 2) + (n & 1)):
        if arr[i] == arr[n - i - 1]:
            if arr[i] != '9':
                if changes[i] == 1 or i == n - i - 1:
                    cost = 1
                else:
                    cost = 2
                if k >= cost:
                    arr[i] = arr[n - i - 1] = '9'
                    k -= cost
    
    return ''.join(arr)

n, k = map(int, input().split())
S = input()
result = highestValuePalindrome(S, n, k)
print(result)