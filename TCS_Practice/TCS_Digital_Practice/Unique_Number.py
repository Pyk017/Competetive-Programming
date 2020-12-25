# Write a program to find the count of numbers which consists of unique digits.

# Input:

# Input consist of two Integer lower and upper value of an range

# Output:

# Output consists of single line, print the count of unique digits in given range. Else Print"No Unique Number"

# Solution:

# Input -

# 10
# 15

# Output : 
# 5



def unique(l, r):
	count = 0
	for i in range(l, r + 1):
		visited = [False for _ in range(10)]
		while i:
			if visited[i % 10]:
				break
			visited[i % 10] = True
			i = i // 10
		if i == 0:
			count += 1

	return count if count > 0 else 'No unique Number'


def unique_pythonic_way(l, r):
	res = list(filter(lambda x: len(str(x)) == len(set(str(x))), range(l, r + 1)))
	return len(res)


l = int(input())
r = int(input())
# result = unique(l, r)
result = unique_pythonic_way(l, r)
print(result)
