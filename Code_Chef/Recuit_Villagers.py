"""
WW3 is near and Gru wants to recruit minions for his team. Gru went to the planet of minions to recruit minions,
he saw that there are two villages separated by a river. He cannot recruit minions from both villages because
then his team will have internal conflicts.

Gru is now in a dilemma about which village to recruit as he wants to have the strongest possible team.

You are given coordinates of houses on the planet. Each house has exactly one minion and his power is given.
The planet of minion is considered as a 2-D plane and the river is denoted by a straight line ( y=mx+c ).
Note: None of the houses are situated on the river.

Input:
First-line will contain N, number of houses.
Second-line will contain two integers, m and c denoting the river.
Next N lines will have exactly 3 integers X[i],Y[i],P[i] denoting the coordinates of houses and the power of minion in
that house.

Output:
Print the maximum power of the team which Gru can recruit.

Sample Input:
3
1 0
0 5 5
0 6 5
0 -8 20

Sample Output:
20
"""


class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calc_points(m, c):
    ls = []
    for i in range(1, 3):
        y = m*i + c
        ls.append(Points(i, y))

    return ls


def is_above(a, b, c):
    return ((b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x)) > 0


n = int(input())
(m, c) = map(int, input().split())
line_a, line_b = calc_points(m, c)
vil1, vil2 = 0, 0
for i in range(n):
    (x, y, p) = map(int, input().split())
    point_c = Points(x, y)
    if is_above(line_a, line_b, point_c):
        vil1 += p
    else:
        vil2 += p

print(max(vil1, vil2))
