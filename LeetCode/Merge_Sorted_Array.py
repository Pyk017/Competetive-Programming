def merge2(m, n, nums1, nums2):
	nums1[:] = sorted(nums1[:m] + nums2)
	return nums1

def merge(m, n, nums1, nums2):
	nums1 += [0 for _ in range(n)]
	x = len(nums1) - 1
	i, j = m - 1, n - 1
	# print(x, i, j)

	while i >= 0 and j >= 0:
		if nums1[i] <= nums2[j]:
			nums1[x] = nums2[j]
			x -= 1
			j -= 1
		else:
			nums1[x] = nums1[i]
			x -= 1
			i -= 1

		# print(nums1)

	while i >= 0:
		nums1[x] = nums1[i]
		i -= 1
		x -= 1

	while j >= 0:
		nums1[x] = nums2[j]
		j -= 1
		x -= 1 

	return nums1




m, n = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
result = merge(m, n, nums1, nums2)
print(*result)