def spiral(a, num):
    sq = num*num
    count, m, n = 0, 0, num
    while count != sq:
        for i in range(m, n):   # For left to right in the matrix
            count += 1
            a[m][i] = count

        for i in range(m+1, n):  # For top to down in the matrix
            count += 1
            a[i][n-1] = count

        for i in range(n-2, m-1, -1):  # For right to left in the matrix
            count += 1
            a[n-1][i] = count

        for i in range(n-2, m, -1):  # For down to top in the matrix
            count += 1
            a[i][m] = count

        m += 1
        n -= 1

    display(a)


def display(a):
    for i in a:
        for j in i:
            print(j, end=" ")

        print()


n = int(input("Enter a Number :- "))
matrix = [[0 for _ in range(n)] for _ in range(n)]
print("Your Spiral Matrix is :- ")
spiral(matrix, n)
