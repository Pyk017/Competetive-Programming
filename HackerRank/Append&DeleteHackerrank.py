s = input()
t = input()
k = int(input())
temp_len, u = 0, 0
for i in range(s):
    if s[i] != t[i]:
        temp_len = len(s[i:])
        u = k - temp_len
        temp_len = len(t[i:])
        u += temp_len
        if u == k:
            print("Yes")
        print("No")
