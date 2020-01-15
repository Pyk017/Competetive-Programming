<<<<<<< HEAD
"""
Sample Input :
4
add hack
add hackerrank
find hac
find hak

Sample Output :
2
0

Explanation :

We perform the following sequence of operations:

1. Add a contact named hack.

2. Add a contact named hackerrank.

3. Find and print the number of contact names beginning with hac.
There are currently two contact names in the application and both of them start with hac, so we print  on a new line.

4. Find and print the number of contact names beginning with hak.
There are currently two contact names in the application but neither of them start with hak, so we print  on a new line.
"""
import collections


def contacts(q):
    result = []
    count = collections.Counter()
    for i, j in q:
        if i in 'add':
            for k in range(1, len(j) + 1):
                count.update([j[0:k]])
        else:
            result.append(count[j])

    return result


queries_row = int(input())
queries = [input().rstrip().split() for _ in range(queries_row)]
res = contacts(queries)
print(' '.join(list(map(str, res))))
=======
"""
Sample Input :
4
add hack
add hackerrank
find hac
find hak

Sample Output :
2
0

Explanation :

We perform the following sequence of operations:

1. Add a contact named hack.

2. Add a contact named hackerrank.

3. Find and print the number of contact names beginning with hac.
There are currently two contact names in the application and both of them start with hac, so we print  on a new line.

4. Find and print the number of contact names beginning with hak.
There are currently two contact names in the application but neither of them start with hak, so we print  on a new line.
"""
import collections


def contacts(q):
    result = []
    count = collections.Counter()
    for i, j in q:
        if i in 'add':
            for k in range(1, len(j) + 1):
                count.update([j[0:k]])
        else:
            result.append(count[j])

    return result


queries_row = int(input())
queries = [input().rstrip().split() for _ in range(queries_row)]
res = contacts(queries)
print(' '.join(list(map(str, res))))
>>>>>>> competetive committed
