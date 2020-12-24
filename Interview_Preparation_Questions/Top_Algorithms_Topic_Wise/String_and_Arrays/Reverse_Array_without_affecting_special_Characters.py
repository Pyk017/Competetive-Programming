import string

# def reverse(st):
#     stack = []
#     for i in st:
#         if i in string.ascii_lowercase:
#             stack.append(i)

#     st = list(st)
#     for i in range(len(st)):
#         if st[i] in string.ascii_lowercase:
#             st[i] = stack.pop()

#     return ''.join(st)


def reverse(st):
    n = len(st)
    l, r = 0, n - 1
    st = list(st)
    while l <= r:
        if not st[l].isalpha():
            l += 1
        if not st[r].isalpha():
            r -= 1
        else:
            st[l], st[r] = st[r], st[l]
            l += 1
            r -= 1

    return st



st = input()
res = reverse(st)
print(res)