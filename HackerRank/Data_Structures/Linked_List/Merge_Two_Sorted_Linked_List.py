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


def merge_lists(head1, head2):
    if not head1 and not head2:
        return None
    elif not head1:
        return head2
    elif not head2:
        return head1
    else:
        if head1.data < head2.data:
            head1.next = merge_lists(head1.next, head2)
            return head1
        else:
            head2.next = merge_lists(head2.next, head1)
            return head2


n = int(input())
link1 = LinkedList()
for _ in range(n):
    link1.insert(int(input()))

m = int(input())
link2 = LinkedList()
for _ in range(m):
    link2.insert(int(input()))

link1.head = merge_lists(link1.head, link2.head)
display(link1.head)
