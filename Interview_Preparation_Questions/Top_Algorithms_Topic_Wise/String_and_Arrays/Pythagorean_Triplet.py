def pythagorean(arr, n):

	arr = [i**2 for i in arr]

	arr.sort()

	for i in range(n - 1, 1, -1):
		l = 0
		r = i - 1
		while l < r:
			if arr[l] + arr[r] == arr[i]:
				print(arr[l], arr[r], arr[i])
				return True
			else:
				if arr[l] + arr[r] < arr[i]:
					l += 1
				else:
					r -= 1

	return False


arr = list(map(int, input().split()))
n = len(arr)
res = pythagorean(arr, n)
print(res)