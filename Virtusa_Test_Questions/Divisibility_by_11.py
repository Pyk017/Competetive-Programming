def divisibility(string):
    even, odd = 0, 0
    for i in range(len(string)):
        if i % 2 == 0:
            even += int(string[i])
        else:
            odd += int(string[i])

    res = abs(even - odd)
    return True if res % 11 == 0 else False

string = input()
print(divisibility(string))