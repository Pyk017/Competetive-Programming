# Write a program to print all the combinations of the given word with or without meaning (when unique characters are given).

# Sample Input:
# abc

# Output:
# abc
# acb
# bac
# bca
# cba
# cab


# Solution:

# Input -
# hai

# Output:
# hai hia ahi aih iah iha


from itertools import permutations

res = []
def permute(s, l, r):
	global res
	if l == r:
		res.append(''.join(s))
	else:
		for i in range(l, r + 1):
			s[l], s[i] = s[i], s[l]
			permute(s, l + 1, r)
			s[l], s[i] = s[i], s[l]


def permute_pythonic_way(s):
	ls = map(lambda x: ''.join(x), list(permutations(s, len(s))))
	print(*list(ls))


string = input()
permute(list(string), 0, len(string) - 1)
print(*res)
# permute_pythonic_way(string)