def alternate(string):
    if string.count('A') == len(string):
        return len(string) - 1
    if string.count('B') == len(string):
        return len(string) - 1
    i = 0
    count = 0
    # while i < len(string) - 1:   # Mine Solution
    #     temp = string[i]
    #     while i < len(string) - 1 and temp == string[i + 1]:
    #         count += 1
    #         i += 1
    #     i += 1

    while i < len(string) - 1:  # Solution better than me
        if string[i] == string[i + 1]:
            count += 1

    return count

            

for _ in range(int(input())):
    string = input()
    res = alternate(string)
    print(res)
