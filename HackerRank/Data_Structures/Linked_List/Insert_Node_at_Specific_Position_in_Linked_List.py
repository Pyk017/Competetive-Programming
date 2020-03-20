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


def insert_node(head, data, pos):
    p = head
    q = None
    node = Node(data)
    for _ in range(pos):
        q = p
        p = p.next

    q.next = node
    node.next = p
    return head


n = int(input())
link = LinkedList()
for _ in range(n):
    link.insert(int(input()))

data = int(input())
pos = int(input())
insert_node(link.head, data, pos)
display(link.head)
