<<<<<<< HEAD
"""
River Sizes:
You are given a two dimentional array of potentially unequal heights and width containing only 1s and 0s. Each 0
represent land, and each 1 represents a part of a river. A consists of any numbers of 1s that are either horizontally
or vertically adjacent(but not diagonally adjacent). The number of adjacent 1s forming a river determine its size. Write
a function that returns an array of the sizes of all rivers represented in the input matrix. Note that these sizes do
not need to be in any particular order.

Sample Input:
[
 [1, 0, 0, 0, 1],
 [1, 0, 1, 0, 0],
 [0, 0, 1, 0, 1],
 [1, 0, 1, 0, 1],
 [1, 0, 1, 1, 0]
]
Sample Output : [1, 2, 2, 2, 5]
"""


def rivers(a):
    marked = set()
    river = []
    count = 0
    for row in range(len(a)):
        for col in range(len(a[row])):
            if a[row][col] == 1 and (row, col) not in marked:
                marked.add((row, col))
                count = 1
                stack = [(row, col)]

                while stack:
                    current = stack.pop()
                    neighbour = get_pos(current, a)
                    for i in neighbour:
                        x, y = i
                        if a[x][y] == 1 and (x, y) not in marked:
                            marked.add((x, y))
                            count += 1
                            stack.append((x, y))

                river.append(count)

    return river


def get_pos(pos, matrix):
    ls = []
    y, x = pos
    if x >= 1: # left
        ls.append((y, x-1))
    if x < len(matrix[0]) - 1:
        ls.append((y, x+1))
    if y >= 1:
        ls.append((y-1, x))
    if y < len(matrix[0]) - 1:
        ls.append((y+1, x))

    return ls


array = [
 [1, 0, 0, 0, 1],
 [1, 0, 1, 0, 0],
 [0, 0, 1, 0, 1],
 [1, 0, 1, 0, 1],
 [1, 0, 1, 1, 0]
]
print(rivers(array))
=======
"""
River Sizes:
You are given a two dimentional array of potentially unequal heights and width containing only 1s and 0s. Each 0
represent land, and each 1 represents a part of a river. A consists of any numbers of 1s that are either horizontally
or vertically adjacent(but not diagonally adjacent). The number of adjacent 1s forming a river determine its size. Write
a function that returns an array of the sizes of all rivers represented in the input matrix. Note that these sizes do
not need to be in any particular order.

Sample Input:
[
 [1, 0, 0, 0, 1],
 [1, 0, 1, 0, 0],
 [0, 0, 1, 0, 1],
 [1, 0, 1, 0, 1],
 [1, 0, 1, 1, 0]
]
Sample Output : [1, 2, 2, 2, 5]
"""


def rivers(a):
    marked = set()
    river = []
    count = 0
    for row in range(len(a)):
        for col in range(len(a[row])):
            if a[row][col] == 1 and (row, col) not in marked:
                marked.add((row, col))
                count = 1
                stack = [(row, col)]

                while stack:
                    current = stack.pop()
                    neighbour = get_pos(current, a)
                    for i in neighbour:
                        x, y = i
                        if a[x][y] == 1 and (x, y) not in marked:
                            marked.add((x, y))
                            count += 1
                            stack.append((x, y))

                river.append(count)

    return river


def get_pos(pos, matrix):
    ls = []
    y, x = pos
    if x >= 1: # left
        ls.append((y, x-1))
    if x < len(matrix[0]) - 1:
        ls.append((y, x+1))
    if y >= 1:
        ls.append((y-1, x))
    if y < len(matrix[0]) - 1:
        ls.append((y+1, x))

    return ls


array = [
 [1, 0, 0, 0, 1],
 [1, 0, 1, 0, 0],
 [0, 0, 1, 0, 1],
 [1, 0, 1, 0, 1],
 [1, 0, 1, 1, 0]
]
print(rivers(array))
>>>>>>> competetive committed
