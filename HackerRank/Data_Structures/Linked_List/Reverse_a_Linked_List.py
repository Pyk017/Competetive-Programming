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
    if head:
        print(head.data)
        display(head.next)


def reverse_list(head):
    p = head
    q = None
    r = p.next
    while p:
        p.next = q
        q = p
        p = r
        try:
            r = r.next
        except AttributeError:
            pass
    head = q
    return head


def reverse_recur(head):
    if not head or not head.next:
        return head
    remain = reverse_recur(head.next)
    head.next.next = head
    head.next = None
    return remain


link = LinkedList()
n = int(input())
for _ in range(n):
    link.insert(int(input()))

link.head = reverse_recur(link.head)
display(link.head)
