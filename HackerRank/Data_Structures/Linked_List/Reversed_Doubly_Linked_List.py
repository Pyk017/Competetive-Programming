class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
                
        self.tail = node

def display(head):
    if head:
        print(head.data)
        display(head.next)

def reverse_list(head):
    p = head
    while p:
        q = p.prev
        p.prev = p.next
        p.next = q
        p = p.prev
    
    if q:    
        head = q.prev
    return head
    

n = int(input())
link = DoublyLinkedList()
for _ in range(n):
    link.insert(int(input()))
link.head = reverse_list(link.head)
display(link.head)