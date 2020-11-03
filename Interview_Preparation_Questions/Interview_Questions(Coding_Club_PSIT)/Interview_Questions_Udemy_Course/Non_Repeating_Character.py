# Given a String we have to find out first non repeating character in that string.
# Input : 'aabbcd'
# Output : 'c'
# Input : 'ababa'
# Output : None

def non_repeating(s):
    di = {}
    temp = ''
    for i in s:
        if i not in di:
            di[i] = 1
        else:
            di[i] += 1
    
    for i, j in di.items():
        if j == 1:
            return i
    return None
    

st = input()
res = non_repeating(st)
print(res)