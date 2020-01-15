<<<<<<< HEAD
"""
Input : geeksforgeeks
Output : No

Input : madam
Output : Yes
"""


def check_palindrome(a):
    ls = list(a)
    i = 0
    while ls:
        if ls[-1] != a[i]:
            return False
        ls.pop()
        i += 1

    return True


string = input("Enter String :- ")
print("Palindrome String!") if check_palindrome(string) else print("Not a Palindrome!")
=======
"""
Input : geeksforgeeks
Output : No

Input : madam
Output : Yes
"""


def check_palindrome(a):
    ls = list(a)
    i = 0
    while ls:
        if ls[-1] != a[i]:
            return False
        ls.pop()
        i += 1

    return True


string = input("Enter String :- ")
print("Palindrome String!") if check_palindrome(string) else print("Not a Palindrome!")
>>>>>>> competetive committed
