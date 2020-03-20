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


def delete(head, pos):
    if pos == 0:
        head = head.next
        return head
    else:
        p = head
        q = None
        for _ in range(pos):
            q = p
            p = p.next

        q.next = p.next
        return head


n = int(input())
link = LinkedList()
for _ in range(n):
    link.insert(int(input()))

posi = int(input())
link.head = delete(link.head, posi)
display(link.head)
