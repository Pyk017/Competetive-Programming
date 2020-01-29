"""
It is an interesting exercise to write a program to print out all permutations of 1,2,…,n. However, since there are
6227020800 permutation of 1,2,..,13 it is unlikely that we would ever run this program on an input of size more than 10.

However, here is another interesting problem whose solution can also be used to generate permutations.
We can order the permutations of 1,2,…,n under the lexicographic (or dictionary) order. Here are the permutations of
1,2,3 in lexicographic order:

123 132 213 231 312 321
The problem we have is the following: given a permutation of 1,2,…,n, generate the next permutation in lexicographic
order. For example, for 2314 the answer is 2341.

Input:
The first line of the input contains two integers, N and K. This is followed by K lines, each of which contains one
permutation of 1,2,…,N.

Output:
The output should consist of K lines. Line i should contain the lexicographically next permutation correponding to the
permutation on line i+1 in the input.

Constraints:
1≤N≤1000.
1≤K≤10.

Sample input
3 2
3 1 2
2 3 1

Sample output
3 2 1
3 1 2
"""
(n, k) = map(int, input().split())
for _ in range(k):
    listing = list(map(int, input().split()))
    i = n - 2
    while i >= 0 and listing[i] >= listing[i + 1]:
        i -= 1
    j = n - 1
    if i >= 0:
        while j > i and listing[j] <= listing[i]:
            j -= 1
        listing[i], listing[j] = listing[j], listing[i]

    listing[i + 1:] = listing[i + 1:][::-1]
    print(*listing)
