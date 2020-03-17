# Sample Input : 07:05:45PM
# Output : 19:05:45


def time_conversion(s):
    if s[-2:] in 'PM':
        if s[:2] in '12':
            s = '12' + s[2:-2]
            return s
        else:
            s = str(12 + int(s[:2])) + s[2:-2]
            return s
    else:
        if s[:2] in '12':
            s = '00' + s[2:-2]
            return s

        return s[:-2]


string = input()
res = time_conversion(string)
print(res)
