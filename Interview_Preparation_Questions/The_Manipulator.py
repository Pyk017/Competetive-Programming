# import string

# d = {string.ascii_uppercase[i]: i for i in range(len(string.ascii_uppercase))}
# t = dict(enumerate(string.ascii_uppercase))

# # print(d)
# # print(t)

# def manipulate(s):
#     st = []
#     for i in s:
#         if i == '#':
#             temp = st.pop()
#             ind = (d[temp] + 1) % 26
#             st.append(t[ind])

#         else:
#             st.append(i)
#     return st

# def manipulates(s1, s2):
#     if s1.count('#') == 0 and s2.count('#') == 0:
#         return 'No'

#     return 'Yes' if manipulate(s1) == manipulate(s2) else "No" 


# for _ in range(int(input())):
#     str1 = input()
#     str2 = input()
#     result = manipulates(str1, str2)
#     print(result)

def calculate(s):
    st = list(s)
    for i in range(len(s)):
        if st[i] == '#':
            for j in range(i - 1, -1, -1):
                if st[j].isalpha():
                    if st[j] == 'Z':
                        st[j] = 'A'
                    else:
                        st[j] = chr(ord(st[j]) + 1)
                    break
    return ''.join(st)
    
for _ in range(int(input())):
    string1 = input()
    string2 = input()
    s1 = calculate(string1)
    s2 = calculate(string2)
    str1 = ''.join(s1.split('#'))
    str2 = ''.join(s2.split('#'))
    if calculate(str1) == calculate(str2):
        print('Yes')
    else:
        print('No')
    