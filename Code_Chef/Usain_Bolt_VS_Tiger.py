"""
Back in 2015, Usain Bolt announced that he'll be retiring after the 2017 World Championship.
Though his final season did not end gloriously, we all know that he is a true legend and we witnessed his peak
during 2008 - 2013.
Post retirement, Usain Bolt is still leading an adventurous life. He's exploring the unexplored parts of the globe.
But sometimes he gets bored, and reads questions asked about him on Quora. One such question he read was,
"Who would win a race between Usain Bolt and a tiger if the race is on a straight line track and the tiger is
distancetoBolt meters behind Bolt? The finishing point is finish meters away from Bolt's starting position.
The tiger starts with an initial speed of 0 meter/second, and will accelerate itself with tigerAccelaration m/s2.
Bolt can run with a constant speed of boltSpeed m/s from start to finish. Given these values,
find out who will win the race - Bolt or the tiger? "

Note that Bolt will win the race if and only if he touches the finishing line before the tiger touches it.
If both of them finish together, the tiger is announced as the winner since Bolt was given an initial advantage.

Since Bolt was busy practicing in the tracks during his Physics school classes, he is asking for your help to solve the
question. Can you please help him?
He just remembers two formulae from the class, and thinks that they will be useful to you:

Displacement(S) = ut +(1/2)at2 where u is the initial velocity , 'a' is the acceleration and t is the time taken.
Velocity = Displacement/Time

Input:
The first line will contain T, the number of testcases. Then the description of each test case follow.
Each test case contains 4 integers finish,distancetoBolt,tigerAccelaration,boltSpeed.

Output:
For each testcase, output in a single line, the word "Bolt" or "Tiger" without quotes, depending on whether Bolt wins or
 the tiger wins.

Constraints
1≤T≤100000
1≤finish≤105
1≤distancetoBolt≤105
1≤tigerAccelaration≤105
1≤boltSpeed≤105

Sample Input:
2
10 100 10 10
100 10 5 10

Sample Output:
Bolt
Tiger
"""


import math


def race(fi, dist_to_bolt, tiger_acc, bolt_sp):
    time_of_bolt = fi // bolt_sp
    time_of_tiger = math.sqrt(2*(dist_to_bolt + fi) // tiger_acc)
    return 'Bolt' if time_of_bolt < time_of_tiger else 'Tiger'


for _ in range(int(input())):
    (finish, distance_to_bolt, tiger_acceleration, bolt_speed) = map(int, input().split())
    print(race(finish, distance_to_bolt, tiger_acceleration, bolt_speed))
