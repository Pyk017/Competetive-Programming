def firstUniqueChar(s):
    d = {}
        if not s:
            return -1
        for i, j in enumerate(s):
            if j not in d:
                d[j] = 1
            else:
                d[j] += 1
            if d[j] == 1:
                res = i
        for k in d:
            if d[k] == 1:
                return s.index(k)
                
        return -1


st = input()
print(firstUniqueChar(st))