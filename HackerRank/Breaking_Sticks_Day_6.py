<<<<<<< HEAD
"""
Sample Input :
3
1 7 24

Output :
55

Explanation : You make 1 move using the stick of length 1, then 8 moves using the stick of length 7, and in the end
46 moves using the stick of length 24. This gives 55 moves in total.
"""
import math


def sticks(n):
    if n == 0 or n == 1:
        return 0
    elif n % 2 == 0:
        return n + sticks(n // 2)
    else:
        temp = math.ceil(math.sqrt(n))
        for k in range(3, temp+2, 2):
            if n % k == 0:
                return n + sticks(n // k)

        return n


num = int(input())
ls = list(map(int, input().split()))
result = 0
for i in ls:
    result += sticks(i) + 1

print(result)
=======
"""
Sample Input :
3
1 7 24

Output :
55

Explanation : You make 1 move using the stick of length 1, then 8 moves using the stick of length 7, and in the end
46 moves using the stick of length 24. This gives 55 moves in total.
"""
import math


def sticks(n):
    if n == 0 or n == 1:
        return 0
    elif n % 2 == 0:
        return n + sticks(n // 2)
    else:
        temp = math.ceil(math.sqrt(n))
        for k in range(3, temp+2, 2):
            if n % k == 0:
                return n + sticks(n // k)

        return n


num = int(input())
ls = list(map(int, input().split()))
result = 0
for i in ls:
    result += sticks(i) + 1

print(result)
>>>>>>> competetive committed
