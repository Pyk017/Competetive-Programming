# Problem Statement:-   You will be given an array of integers and a target value. Determine the number of pairs of array elements that have 
# 						a difference equal to a target value.


# For example:- given an array of [1, 2, 3, 4] and a target value of 1, we have three values meeting the condition: 
# 				2-1 = 1, 3-2 = 1, and 4-3 = 1.


# Function Description
# Write a function pairs. It must return an integer representing the number of element pairs having the required difference.

# pairs has the following parameter(s):

# k: an integer, the target difference
# arr: an array of integers
# Input Format

# The first line contains two space-separated integers n and k, the size of arr and the target value.
# The second line contains n space-separated integers of the array arr.
# Sample Input

#      5 2

#      1 5 3 4 2 

# Sample Output

#      2


def func(a, n, t):
	count = 0
	d = {i: 0 for i in a}
	for j in a:
		if d[j] == 0 and d[j+t] == 0:
			d[j] = 1
			d[t + j] = 1
			count += 1

	print(d)


	return count


def two_pointer_approach(a, n, t):
	i, j = 0, 1
	count = 0
	a.sort()
	while i < n and j < n:
		if i != j and a[j] - a[i] == t:
			print(a[i], a[j])
			count += 1
			i += 1
			j += 1
		elif a[j] - a[i] < t:
			j += 1
		else:
			i += 1

	return count


n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
# res = func(arr, n, target)
res = two_pointer_approach(arr, n, target)
print(res)
