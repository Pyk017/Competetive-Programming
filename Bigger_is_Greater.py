def next_permutation(s):
    i = len(s) - 1
    while i >= 0 and s[i - 1] >= s[i]:
        i -= 1
    
    if i <= 0:
        return 'no answer'

    j = len(s) - 1
    
    while s[j] <= s[i - 1]:
        j -= 1

    s[i - 1], s[j] = s[j], s[i - 1]
    s[i:] = reversed(s[i:])

    return ''.join(s)
        


string = input()
res = next_permutation(list(string))
print(res)