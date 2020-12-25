# import  collections

# def solution(s):
#     n = len(s)
#     res = 0
#     for i in range(n):
#         d = collections.defaultdict(int)
#         odd = 0
#         for j in range(i, n):
#             d[s[j]] += 1
#             if d[s[j]] % 2 == 0:
#                 odd -= 1
#             else:
#                 odd += 1
#             if odd <= 1:
#                 res += 1
#     return res


# print(solution("ABAB"))

# def decode(s):
#     if len(s) == 1:
#         return 1
#     elif len(s) == 2:
#         return 2

#     temp = 2
#     res = 1
#     for i in range(len(s) - 1):
#         if int(s[i: temp])  <= 52:
#             res += 1
#         temp += 1
#     return res



# st = input()
# print(decode(st))




# class Solution {
# public:
#     int numDecodings(string s) {
#         int prev = 1, cur = 1;
        
#         for (int i = 0; i < s.size(); ++i) {
#             int next = [&] {
#                 if (s[i] == '0') 
#                     return i > 0 && (s[i-1] == '1' || s[i-1] == '2') ? prev : 0;
#                 else
#                     return i > 0 && ((s[i] <= '9' && s[i-1] == '1') || (s[i] <= '6' && s[i-1] == '2')) ? prev + cur : cur;
#             }();
            
#             prev = cur, cur = next;
#         }
        
#         return cur;
#     }
# };




# def func(s, i, p, c):
#     if s[i] == '0':
#         return p if i > 0 and (s[i - 1] == '1' or s[i - 1] == '2') else 0
#     else:
#         return (p + c) if i > 0 and ((s[i] <= '9' and s[i - 1] == '1') or (s[i] <= '6' and s[i - 1] == '2')) else c


# def decode(s):
#     prev, curr = 1, 1
#     for i in range(len(s)):
#         temp = func(s, i, prev, curr)
#         prev = curr
#         curr = temp

#     return curr

def decode(s):
    if not s or s[0] == '0':
        return 1
    if len(s) == 1:
        return 1
    elif len(s) == 2:
        return 2
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(1, n):
        if s[i] != '0':
            dp[i+1] += dp[i]
        if s[i-1] != '0' and 1 <= int(s[i-1:i+1]) <= 52:
            dp[i+1] += dp[i-1]
    return dp[n]


st = input()
print(decode(st))















# def maxArea(height):

#     result, p1, p2 = 0, 0, len(height)-1

#     while p1 < p2:
#         result = max(result, (p2 - p1)*min(height[p1], height[p2]))
#         if height[p1] > height[p2]: 
#             p2 -= 1
#         else: 
#             p1 += 1

#     return result


# ls = list(map(int, input().split(',')))
# print(maxArea(ls))








