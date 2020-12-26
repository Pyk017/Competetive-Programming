class Heap(object):
	def __init__(self, arr):
		self.arr = arr
		self.heapsize = len(arr)

	def heapify(self, i):
		left = 2 * i + 1
		right = 2 * i + 2
		if left < self.heapsize and self.arr[left] > self.arr[i]:
			largest = left
		else:
			largest = i

		if right < self.heapsize and self.arr[right] > self.arr[largest]:
			largest = right

		if largest != i:
			self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
			self.heapify(largest)


	def build_max_heap(self):
		self.heapsize = len(self.arr)
		for i in range(len(self.arr) // 2 - 1, -1, -1):
			self.heapify(i)


	def heapsort(self):
		self.build_max_heap()
		for i in range(len(self.arr)-1, 0, -1):
			self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
			self.heapsize -= 1
			self.heapify(0)

		return self.arr


	def extract_max(self):
		if self.heapsize < 0:
			return "Heap Overflow"

		maxi = self.arr[0]
		self.arr[0] = self.arr[self.heapsize - 1]
		self.heapsize -= 1
		self.heapify(0)
		return maxi


	def increase_key(self, i, key):
		if key < self.arr[i]:
			return False

		self.arr[i] = key
		while i >= 0 and self.arr[i // 2] < self.arr[i]:
			self.arr[i], self.arr[i // 2] = self.arr[i // 2], self.arr[i]
			i = i // 2

		return True



arr = list(map(int, input().split()))
heap = Heap(arr)
result = heap.heapsort()
print(result)
