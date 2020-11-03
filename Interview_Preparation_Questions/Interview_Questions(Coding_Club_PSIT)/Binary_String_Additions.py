# Given two binary strings, return their sum(also a binary number). The input strings are both non-empty and contains
# only characters 1 or 0.
# Input : a = '11' b = '1'
# Output : '100'

str1 = int(input("Enter First String :- "))
str2 = int(input('Enter Second String :- '))


def binary_to_decimal(binary):
    sumi = 0
    binary = str(binary)[::-1]
    for i in range(len(binary)):
        if binary[i] == '1':
            sumi += 2**i

    return sumi


def decimal_to_binary(dec):
    new_str = ''
    while dec != 0:
        mod = dec % 2
        new_str = str(mod) + new_str
        dec = dec // 2

    return int(new_str)


ans = binary_to_decimal(str1) + binary_to_decimal(str2)
print("Your Binary Addition value is :- ", decimal_to_binary(ans), ans)
