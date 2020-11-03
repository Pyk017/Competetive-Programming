def first(a):
    s = set()
    for i in a:
        if i not in s:
            s.add(i)
        else:
            break
    
    return i
    
a = [2, 1, 3, 5, 3, 2]
print(first(a))