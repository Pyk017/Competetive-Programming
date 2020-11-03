import sys
maxi = -sys.maxsize
string = input()
res = 0
for i in range(len(string) // 2):
    if string.endswith(string[: i + 1]):
        res = i + 1
        maxi = max(maxi, res)
        
print('-1') if res == 0 else print(maxi)