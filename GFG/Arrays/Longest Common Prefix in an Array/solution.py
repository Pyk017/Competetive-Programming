import sys

class Solution:
    def longestCommonPrefix(self, arr, n):
        
        
        if n == 1: 
            return arr[0]
        
        flag = False
        first = arr[0]
        mini = sys.maxsize
        ans = ""
        i = 0
        
        for string in arr[1:]:
            i = 0
            while i < len(string):
                if i >= len(first):
                    break
                
                if (string[i] != first[i]):
                    break
                
                i += 1
            
            if i == 0:
                return -1
            
            if i <= mini:
                ans = string[:i] 
                mini = i
            
        
        return ans
        

            

if __name__=='__main__':    
    n = int(input())
    arr = [x for x in input().strip().split(" ")]
    
    ob=Solution()
    print(ob.longestCommonPrefix(arr, n))