def expand_from_middle(s, left, right):
    if not s or left > right:
        return 0

    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1


def longest_palindrome(S):
    if not S or len(S) < 1:
        return ''
    start, end = 0, 0
    for i in range(len(S)):
        l1 = expand_from_middle(S, i, i)
        l2 = expand_from_middle(S, i, i + 1)
        l = max(l1, l2)
        if l > end - start:
            start = i - ((l - 1) // 2)
            end = i + (l // 2)

    return S[start: end + 1]


n = int(input())
string = input()
res = longest_palindrome(string)
print(len(res))
print(res)
# maxi = ''
# for i in range(n):
#     for j in reversed(range(n)):
#         b = string[i: j+1]
#         if b == b[::-1]:
#             if len(b) > len(maxi):
#                 maxi = b
#
# print(len(maxi))
# print(maxi)
