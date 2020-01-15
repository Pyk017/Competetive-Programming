<<<<<<< HEAD
"""
Find the winner of the Game to Win by erasing any two consecutive similar alphabets .
Given a string consisting of lower case alphabets.
Rules of the Game:
1. A player can choose a pair of similar consecutive characters and erase them.
2. There are two players playing the game, the players who makes the last move wins,
The task is to find the winner if A goes first and both play optimally.
Input : 'kaak'
Output : B
Explanation : A's turn remove 'aa' thus the remaining string 'kk'
B's turn remove 'kk' now remaining string ''. So, B won.
"""


def game(a):
    count = 0
    stack = [a[0]]
    for i in range(1, len(a)):
        if a[i] == stack[-1]:
            count += 1
            stack.pop()
        else:
            stack.append(a[i])
            
    return 'B' if count % 2 == 0 else 'A'


string = input('Enter a String :- ')
print('Winner is :- ', game(string))
=======
"""
Find the winner of the Game to Win by erasing any two consecutive similar alphabets .
Given a string consisting of lower case alphabets.
Rules of the Game:
1. A player can choose a pair of similar consecutive characters and erase them.
2. There are two players playing the game, the players who makes the last move wins,
The task is to find the winner if A goes first and both play optimally.
Input : 'kaak'
Output : B
Explanation : A's turn remove 'aa' thus the remaining string 'kk'
B's turn remove 'kk' now remaining string ''. So, B won.
"""


def game(a):
    count = 0
    stack = [a[0]]
    for i in range(1, len(a)):
        if a[i] == stack[-1]:
            count += 1
            stack.pop()
        else:
            stack.append(a[i])
            
    return 'B' if count % 2 == 0 else 'A'


string = input('Enter a String :- ')
print('Winner is :- ', game(string))
>>>>>>> competetive committed
