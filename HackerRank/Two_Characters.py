def check(s):
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            return False
    return True
    
    
def alternate(s):
    maxi = -1
    unique = list(set(s))
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            temp = [k for k in s if k == unique[i] or k == unique[j]]
            if check(temp):
                maxi = max(maxi, len(temp))
                
    return maxi
    
n = int(input())
string = input()
print(alternate(string))