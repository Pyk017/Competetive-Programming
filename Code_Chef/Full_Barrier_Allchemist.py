"""
Edward Elric is chasing after Scar. To stop Edward, Scar creates N barriers in the way, numbered from 1 to N.
Each barrier Scar created is either one of the following two types.

Type 1 barrier - This barrier start from a height X above the ground and extend till the sky.
Type 2 barrier - This barrier start from the ground and extend up to height X above the ground.

The height of Edward is H units and he has an alchemic life force of L units. Moreover, he can duck by Y1 units and jump
by height Y2 units (as explained in the figures). He starts crossing barriers in sequence, starting from barrier 1 till
the barrier N. Whenever he can't pass a barrier by ducking or jumping
(considered passed even when the barrier just touches him), he uses Alchemy to break the barrier.
However, this costs him a single unit of his alchemic life force.

If after breaking a barrier no life force is left, Edward gets completely exhausted, unable to pass that barrier.
How many barriers can Edward cross?

And remember never to call him a pipsqueak if his height is too short!

Input:
The first line contains T, the number of test cases. Then the test cases follow.
For each test case, the first line contains five integers N, H, Y1, Y2 and L.
The next N lines, each contain two integers ti and Xi for the ith barrier where ti=1 denotes a Type 1 Barrier and ti=2
denotes a Type 2 barrier.

Output:
For each test case print a single line containing the number of barriers Edward can pass.

Constraints
1≤T≤100
1≤N≤103
2≤H≤103
1≤Y1<H
1≤Y2≤103
1≤L≤N
1≤ti≤2
1≤Xi≤103

Sample Input:
3
6 5 1 2 3
2 2
2 1
1 10
2 8
2 4
1 2
1 4 2 5 1
2 6
6 5 1 2 3
2 2
2 1
1 10
2 8
2 4
1 6

Sample Output:
5
0
6

Explanation:
Test Case 1:
Given N=6, H=5, Y1=1, Y2=2 and L=3.
He passes the first three barriers by either ducking or jumping. He uses alchemic life force for breaking 4th, 5th and
6th barrier because he cannot pass them by either jumping or ducking. He gets exhausted after breaking the 6th barrier
and is unable to pass it. So, in total he passes 5 barriers.
"""


def alchemist(listing, n, h, y1, y2, lf):
    count, i = 0, 0
    while i < n and lf != 0:

        if listing[i][0] == 1:
            if listing[i][1] >= (h - y1):
                count += 1
            else:
                lf -= 1
                count += 1

        elif listing[i][0] == 2:
            if listing[i][1] <= y2:
                count += 1
            else:
                lf -= 1
                count += 1

        i += 1

    if lf == 0:
        return count - 1

    return count


for _ in range(int(input())):
    (N, H, Y1, Y2, L) = map(int, input().split())
    array = []
    for _ in range(N):
        (T, X) = map(int, input().split())
        array. append((T, X))

    print(alchemist(array, N, H, Y1, Y2, L))
