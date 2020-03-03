def append_and_delete(str1, str2, _k):
    i = 1
    for i in reversed(range(1, _k+1)):
        if str1 == str2[:len(str1)] and len(str2) - len(str1) == i or len(str1) == 0:
            break
        str1 = str1[:-1]

    if len(str2) - len(str1) <= i:
        return 'Yes'
    return 'No'


string1 = input()
string2 = input()
k = int(input())
print(append_and_delete(string1, string2, k))
