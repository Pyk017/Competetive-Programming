<<<<<<< HEAD
"""
Minimum Operations required to make all elements distinct in an array.
Given an array of N integers. If a number occurs more than once, choose any number y from the array and replace the x
in the array to x+y such that x+y is not in the array. The task is to find the minimum number of operations to make
the array a distinct one.
Input : [2, 1, 2]
Output : 1
Explanation : x = 2 , y = 1 then replace 2 by 3.
Performing the above step make all the elements in the array distinct

Input : [1, 2, 3]
Output : 0
"""
from collections import Counter


def distinct(a):
    dic = dict(Counter(a))
    count = 0
    for i, j in dic.items():
        while j > 1:
            count += 1
            dic[i] -= 1
            j -= 1

    return count


array = list(map(int, input('Enter elements in the Array :- ').split()))
print(distinct(array))
=======
"""
Minimum Operations required to make all elements distinct in an array.
Given an array of N integers. If a number occurs more than once, choose any number y from the array and replace the x
in the array to x+y such that x+y is not in the array. The task is to find the minimum number of operations to make
the array a distinct one.
Input : [2, 1, 2]
Output : 1
Explanation : x = 2 , y = 1 then replace 2 by 3.
Performing the above step make all the elements in the array distinct

Input : [1, 2, 3]
Output : 0
"""
from collections import Counter


def distinct(a):
    dic = dict(Counter(a))
    count = 0
    for i, j in dic.items():
        while j > 1:
            count += 1
            dic[i] -= 1
            j -= 1

    return count


array = list(map(int, input('Enter elements in the Array :- ').split()))
print(distinct(array))
>>>>>>> competetive committed
