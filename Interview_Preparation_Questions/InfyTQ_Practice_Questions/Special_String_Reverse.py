import string
special = string.punctuation

string = list(input())
i = 0
j =  len(string) - 1
while i < len(string) and j >= 0 and i < j:
    # print(i, j)
    if string[i] not in special and string[j] not in special:
        string[i], string[j] = string[j], string[i]
        i += 1
        j -= 1
    elif string[i] in special:
        i += 1
    else:
        j -= 1
print(''.join(string))
