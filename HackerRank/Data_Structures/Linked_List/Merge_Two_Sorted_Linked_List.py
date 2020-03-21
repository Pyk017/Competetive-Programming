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


def insert_here(head, data):
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


def merge_lists(head1, head2, head3):
    if not head1:
        return head2
    elif not head2:
        return head1
    else:
        while head1 or head2:
            try:
                if head1 != None and (head1.data <= head2.data or head2 == None):
                    head3 = insert_here(head3, head1.data)
                    head1 = head1.next
                else:
                    head3 = insert_here(head3, head2.data)
                    head2 = head2.next
            except AttributeError:
                pass    
    return head3


n = int(input())
link1 = LinkedList()
for _ in range(n):
    link1.insert(int(input()))

m = int(input())
link2 = LinkedList()
for _ in range(m):
    link2.insert(int(input()))
link3 = LinkedList()
link3.head = merge_lists(link1.head, link2.head, link3.head)
display(link3.head)
