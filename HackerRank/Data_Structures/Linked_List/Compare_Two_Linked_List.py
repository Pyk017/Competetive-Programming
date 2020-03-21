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


def compare_lists(head1, head2):
    if not head1 or not head2:
        return 0
    else:
        while head1 and head2:
            if head1.data != head2.data:
                return 0
            head1 = head1.next
            head2 = head2.next

        if head1 or head2:
            return 0
        return 1


n = int(input())
link1 = LinkedList()
for _ in range(n):
    link1.insert(int(input()))

m = int(input())
link2 = LinkedList()
for _ in range(m):
    link2.insert(int(input()))

res = compare_lists(link1.head, link2.head)
print(res)
