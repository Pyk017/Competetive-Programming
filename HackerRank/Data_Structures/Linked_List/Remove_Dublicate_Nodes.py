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


def remove_dublicate(head):
    p = head
    q = p.next
    while q:
        if p.data == q.data:
            p.next = q.next 
            q = p.next
        else:
            p = q
            q = q.next
    return head

n = int(input())
link = LinkedList()
for _ in range(n):
    link.insert(int(input()))
link.head = remove_dublicate(link.head)
display(link.head)
