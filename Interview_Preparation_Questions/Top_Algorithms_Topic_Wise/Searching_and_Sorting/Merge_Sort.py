def merge(ar, left, mid, right):

	L = ar[left: mid + 1]
	R = ar[mid + 1: right + 1]

	n1 = len(L)
	n2 = len(R)

	i, j, k = 0, 0, left
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			ar[k] = L[i]
			i += 1
		else:
			ar[k] = R[j]
			j += 1
		k += 1


	while i < n1:
		ar[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		ar[k] = R[j]
		j += 1
		k += 1



def merge_sort(arr, left, right):
	if left < right:
		mid = (left + right) // 2
		merge_sort(arr, left, mid)
		merge_sort(arr, mid + 1, right)
		merge(arr, left, mid, right)

	return arr


arr = list(map(int, input().split()))
n = len(arr)
result = merge_sort(arr, 0, n - 1)
print(*result)



# ------------------------ Another Function --------------------------

# def merge(arr):
# 	if len(arr) <= 1:
# 		return arr

# 	mid = len(arr) // 2
# 	L = arr[:mid]
# 	R = arr[mid:]

# 	merge(L)
# 	merge(R)

# 	i, j, k = 0, 0, 0

# 	while i < len(L) and j < len(R):
# 		if L[i] < R[j]:
# 			arr[k] = L[i]
# 			i += 1
# 		else:
# 			arr[k] = R[j]
# 			j += 1
# 		k += 1


# 	while i < len(L):
# 		arr[k] = L[i]
# 		i += 1
# 		k += 1

# 	while j < len(R):
# 		arr[k] = R[j]
# 		j += 1
# 		k += 1



# arr = list(map(int, input().split()))
# n = len(arr)
# merge(arr)
# print(*arr)
