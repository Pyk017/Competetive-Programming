# There is a range given n and m in which we have to find the count all the prime pairs whose difference is 6. 
# We have to find how many sets are there within a given range.

# Output:

# Output consists of single line, print the count prime pairs in given range. Else print"No Prime Pairs".

# Constraints:

# 2<=n<=1000
# n<=m<=2000


# Sample Input:

# 4
# 30

# Output:

# 6

# Explanation:

# (5, 11) (7, 13) (11, 17) (13, 19) (17, 23) (23, 29) . we have 6 prime pairs.

# Solution:

# Input -

# 101
# 500

# Output:

# 30



def is_Prime(n):
	if n == 2 or n == 3:
		return True
	elif n == 0 or n == 1:
		return False

	i = 2
	while (i * i) <= n:
		if n % i == 0:
			return False

		i += 1

	return True


def prime_pairs(l, r):
	ls = [0 for i in range(r + 1)]
	for i in range(l, r + 1):
		if is_Prime(i):
			ls[i] = 1

	res = []
	# print(ls)
	for i in range(l, r + 1 - 6):
		if ls[i] and ls[i + 6]:
			res.append((i, i + 6))

	# print(res)
	return len(res)


l = int(input())
r = int(input())
result = prime_pairs(l, r)
print(result)
