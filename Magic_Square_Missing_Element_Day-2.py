"""
Fill missing entries of a magic square.
Given a 3X3 matrix 'mat' with it's left diagonal elements missing (set to 0). considering the sum of every row, column
and diagonal of the original matrix was equal, the task is to find the missing diagonal elements and print the original
matrix.
Input : [[0, 7, 6], [9, 0, 1], [4, 3, 0]]
Output :
2 7 6
9 5 1
4 3 8
Row Sum = Column Sum = Diagonal Sum = 15
"""


def find_missing(a):
    su, row_sum = 0, 0
    for i in a:
        for j in i:
            su += j

    su //= 2
    for i in range(len(a)):
        row_sum = 0
        for j in range(len(a[i])):
            row_sum += a[i][j]

        a[i][i] = su - row_sum

    print("New Matrix is :- ")
    for i in a:
        for j in i:
            print(j, end=" ")
        print()


n = int(input("Enter Range :- "))
print('Enter elements in the Matrix :- ')
ls = [list(map(int, input().split())) for _ in range(n)]
find_missing(ls)
