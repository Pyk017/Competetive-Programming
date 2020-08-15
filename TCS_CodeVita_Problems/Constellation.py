'''
Three characters { #, *, . } represents a constellation of stars and galaxies in space. Each galaxy is demarcated by # characters. There can be one or many stars in a given galaxy. Stars can only be in shape of vowels { A, E, I, O, U } . A collection of * in the shape of the vowels is a star. A star is contained in a 3x3 block. Stars cannot be overlapping. The dot(.) character denotes empty space.

Given 3xN matrix comprising of { #, *, . } character, find the galaxy and stars within them.

Note: Please pay attention to how vowel A is denoted in a 3x3 block in the examples section below.

Constraints

3 <= N <= 10^5

Input

Input consists of single integer N denoting number of columns.

Output

Output contains vowels (stars) in order of their occurrence within the given galaxy. Galaxy itself is represented by # character.


Example 1

Input

18

* . * # * * * # * * * # * * * . * .

* . * # * . * # . * . # * * * * * *

* * * # * * * # * * * # * * * * . *

Output

U#O#I#EA

Explanation

As it can be seen that the stars make the image of the alphabets U, O, I, E and A respectively.


Example 2

Input

12

* . * # . * * * # . * .

* . * # . . * . # * * *

* * * # . * * * # * . *

Output

U#I#A

Explanation

As it can be seen that the stars make the image of the alphabet U, I and A.

Possible solution:

Input:

12

* . * # . * * * # . * .

* . * # . . * . # * * *

* * * # . * * * # * . *

'''

n = int(input())
galaxy = [list(map(int, input().split())) for _ in range(3)]

for i in range(n):
    if galaxy[0][i] == '#' and galaxy[1][j] == '#' and galaxy[2][i] == '#':
        print('#', end='')
    elif galaxy[0][i] == '.' and galaxy[1][j] == '.' and galaxy[2][i] == '.':
        pass
    else:

        x = i
        a, b, c, a1, b1, c1, a2, b2, c2 = galaxy[0][x], galaxy[0][x+1], galaxy[0][x+2], galaxy[1][x], galaxy[1][x+1], galaxy[1][x+2], galaxy[2][x], galaxy[2][x+1], galaxy[2][x+2]
        if a == '.' and b == '*' and c == '.' and a1=='*' and b1 == '*' and c1 == '*' and a2=='*' and b2 == '.' and c2 == '*':              		
      		print("A", end='')
      		i = i + 2
      	
      	if a == '*' and b == '*' and c == '*' and a1 == '*' and b1 == '*' and c1 == '*' and a2 == '*' and b2 == '*' and c2 == '*':
      		print("E", end='')
      		i = i + 2
      	
      	if a == '*' and b == '*' and c == '*' and a1 == '.' and b1 == '*' and c1 == '.' and a2 == '*' and b2 == '*' and c2 == '*':
	  		print("I", end='')
      		i = i + 2

      	if a == '*' and b == '*' and c == '*' and a1 == '*' and b1 == '.' and c1 == '*' and a2 == '*' and b2 == '*' and c2 == '*':
	  		print("O", end='')
      		i = i + 2

      	if a == '*' and b == '.' and c == '*' and a1 == '*' and b1 == '.' and c1 == '*' and a2 == '*' and b2 == '*' and c2 =='*':  		
      		print("U", end='')
      		i = i + 2
      		