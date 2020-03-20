class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def display(head):
    p = head
    while p:
        print(p.data)
        p = p.next


def reverse_display(head):
    if head:
        reverse_display(head.next)
        print(head.data)


n = int(input())
link = LinkedList()
for _ in range(n):
    link.insert(int(input()))

# display(link.head)
reverse_display(link.head)
