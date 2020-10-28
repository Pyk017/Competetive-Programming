def cipher(string, key):
    if key < 0:
        return 'INVALID INPUT!'
    result = ""
    for i in string:
        # print(ord(i))
        if ord(i) in range(65, 91):
            result += chr((((ord(i) + key) - 65) % 26) + 65)
        elif ord(i) in range(97, 123):
            result += chr((((ord(i) + key) - 97) % 26) + 97)
        elif ord(i) in range(48, 58):
            result += chr((((ord(i) + key) - 48) % 10) + 48) 
        # print(result)
        else:
            result += i
        

    return result

string = input()
key  = int(input())
res = cipher(string, key)
print(res)
