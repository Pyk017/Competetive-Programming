# import sys 
# def segment(x, space):
#     arr = space
#     k = x 
#     mini = sys.maxsize 
#     maxi = -sys.maxsize
    
#     for i in range(n - k + 1): 
#         mini = arr[i] 
#         for j in range(1, k): 
#             if arr[i + j] < mini: 
#                 mini = arr[i + j] 

#         maxi = max(maxi, mini)
#     return maxi

# n, x = map(int, input().split())
# ar = list(map(int, input().split()))
# res = printMax(ar, n, x)
# print(res)


# def printMaxOfMin(arr, n, k): 
      
#     s = [] 
#     left = [-1] * (n + 1)  
#     right = [n] * (n + 1)  
  
#     for i in range(n): 
#         while (len(s) != 0 and 
#                arr[s[-1]] >= arr[i]):  
#             s.pop()  
  
#         if (len(s) != 0): 
#             left[i] = s[-1] 
  
#         s.append(i) 

#     while (len(s) != 0): 
#         s.pop() 
  
#     for i in range(n - 1, -1, -1): 
#         while (len(s) != 0 and arr[s[-1]] >= arr[i]):  
#             s.pop()  
  
#         if(len(s) != 0):  
#             right[i] = s[-1]  
  
#         s.append(i) 
    
#     # print(left, right)
#     ans = [0] * (n + 1) 
    
  
    
#     for i in range(n): 
#         Len = right[i] - left[i] - 1
#         ans[Len] = max(ans[Len], arr[i]) 
    
#     # print(ans)
#     for i in range(n - 1, 0, -1): 
#         ans[i] = max(ans[i], ans[i + 1])  
  
#     return ans[k]
  

# if __name__ == '__main__': 
  
#     n, x = map(int, input().split())
#     ar = list(map(int, input().split()))
#     res = printMaxOfMin(ar, n, x)
#     print(res)



import re

pattern = '\[[0-9][0-9]/[a-zA-z]+/[0-9][0-9][0-9][0-9]:[0-9][0-9]:[0-9][0-9]:[0-9][0-9] -[0-9][0-9][0-9][0-9]\]'
r = re.compile(pattern)


with open("t1.txt", 'r') as f:
    s = f.read()
    result = r.findall(s)


with open("t2.txt", 'w') as f2:
    f2.write('\n'.join(result))

    # print(type(f.read()))




# [01/Jul/1995:00:00:06 -0400]
