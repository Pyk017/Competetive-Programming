class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def display(head):
    if head:
        print(head.data)
        display(head.next)


def insert(head, data):
    node = Node(data)
    if not head:
        return node
    p = head
    q = None
    while p:
        q = p
        p = p.next
    q.next = node
    return head


n = int(input())
link = LinkedList()
for _ in range(n):
    link.head = insert(link.head, int(input()))
display(link.head)
