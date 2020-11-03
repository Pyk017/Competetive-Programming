"""
Starting from 1 assign an alphabet to each integer, for eg. if input is 1 then A should be the Output, 2=B, 3=C ... 26=Z
Similarly, 27=AA, 28=AB, ...., 52=AZ, 702=ZZ,  703=AAA and so on.
"""

from string import ascii_uppercase
ls = dict(enumerate(ascii_uppercase, 1))


def convert_alphabet(inp):
    new_str = ''
    while inp != 0:
        rem = inp % 26
        new_str = ls[rem] + new_str
        inp //= 26

    return new_str


num = int(input("Enter a Number :- "))
print("Equivalent Alphabet is :- ", convert_alphabet(num))

