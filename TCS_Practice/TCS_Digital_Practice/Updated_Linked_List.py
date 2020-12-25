class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.after = None

	def add_node(self, data):
		temp = Node(data)
		if not self.head:
			self.head = temp
			self.after = temp

		else:
			self.after.next = temp
			self.after = temp

	def display(self):
		p = self.head
		while p:
			print(p.value, end=' ')
			p = p.next


def update_linked_list(head):
	p = head
	count = 0
	stack = []
	while p:
		count += 1
		stack.append(p.value)
		p = p.next

	p = head 
	i = 0	
	while p:
		if count % 2 == 0:
			p.value = p.value + stack.pop()
		else:
			if i == (count // 2):
				stack.pop()
				pass
			else:
				p.value = p.value + stack.pop()	
		i += 1
		p = p.next

	return head



ll = LinkedList()
input_arr = list(map(lambda x: ll.add_node(int(x)), input().split()))
# ll.display()
# print()
ll.head = update_linked_list(ll.head)
ll.display()


