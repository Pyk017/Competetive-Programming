def match(s1, s2):
    d = {i: 0 for i in s1}
    for j in s2:
        if j in d:
            return 'YES'
    return "NO"

 
for _ in range(int(input())):
    string1 = list(input())
    string2 = list(input())
    res = match(string1, string2)
    print(res)
