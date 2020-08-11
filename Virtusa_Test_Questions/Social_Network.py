def divisibilityCheck(n): 
    
    s = {i: 1 for i in range(2, n + 2)} 
    max_ele = n + 2
    arr = [i for i in range(2, n + 2)]
    
    res = dict() 
    
    for i in range(len(arr)):  
        for j in range(arr[i] * 2,  max_ele + 1, arr[i]): 
            if (j in s.keys()): 
                res[j] = 1
                res[arr[i]] = 1
              
    return len(s) - len(res)


n = int(input()) 
res = divisibilityCheck(n) 
print(res + 1)












# # Python program 
  
# # import sys 
# # This function prints the longest palindrome 
# # substring of st[]. It also returns the length 
# # of the longest palindrome 
# def maxarray(input1, input2) : 
#     n = input1 
#     if n == 1 or len(set(input2)) == n:
#         return -1
    
#     table = [[0 for x in range(n)] for y 
#                           in range(n)]  
      
#     maxLength = 1
#     i = 0
#     while (i < n) : 
#         table[i][i] = True
#         i = i + 1
      
    
#     start = 0
#     i = 0
#     while i < n - 1 : 
#         if (input2[i] == input2[i + 1]) : 
#             table[i][i + 1] = True
#             start = i 
#             maxLength = 2
#         i = i + 1

#     k = 3
#     while k <= n :  
#         i = 0
#         while i < (n - k + 1) : 
#             j = i + k - 1
#             if (table[i + 1][j - 1] and 
#                       input2[i] == input2[j]) : 
#                 table[i][j] = True
      
#                 if (k > maxLength) : 
#                     start = i 
#                     maxLength = k 
#             i = i + 1
#         k = k + 1
#     # print ("Longest palindrome substring is: ", st[start: start + maxLength]) 
  
#     return input2[start: start + maxLength] 
  
  
# st = input()
# l = maxarray(len(st), st) 
# print ("Length is:", l) 





















