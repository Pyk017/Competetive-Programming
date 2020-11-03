"""
Write an algorithm to determine if a number is 'happy'. A Happy Number is a number defined by the following process :
Starting with any positive integer, replace the number by the sum of squares of its digits, and repeat the process until
the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for
which this process ends in 1's are Happy Number.
Input : 19
Output : True
Explanation :
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^0 + 0^0 + 0^0 = 1
Thus, 19 is a Happy Number.
"""


def sum_of_square(ls):
    return sum(list(map(lambda x: x**2, ls)))


def happy(num):
    if num == 1:
        return True
    elif 1 < num <= 9 or num == 0:
        return False
    else:
        return happy(sum_of_square(list(map(int, str(num)))))


# number = int(input("Enter a number :- "))
# print("Number is a Happy Number") if happy(number) else print("Number is not a Happy Number")
ran = int(input("Enter Range :- "))
print("Happy Numbers within your range are :- ")
for i in range(1, ran+1):
    if happy(i):
        print(i, end=' ')
