def isPalindrome(string):
	return string == string[::-1] 


def partitions(result, curr, start, n, string):
	 if start >= n:
	 	result.append(curr[:])
	 	return 

	 for i in range(start, n):
	 	if isPalindrome(string[start: i + 1]):
	 		curr.append(string[start: i + 1])
	 		# print(string[start: i + 1])
	 		partitions(result, curr, i + 1, n, string)
	 		# print(result, curr)
	 		curr.pop()


def possiblePartitions(string):
	start = 0
	n =  len(string)
	curr = []
	result = []
	partitions(result, curr, start, n, string)
	for i in result:
		print(*i)
	return result


st = input()
res = possiblePartitions(st)
print(res)