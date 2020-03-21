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

def sorted_insert(head, tar):
    node = Node(tar)
    if tar < head.data:
           node.next = head
           head = node
           return head

    else:
        p = head
        q = None
        while p and p.data < tar:
            q = p
            p = p.next
        
        if p:
            node.prev = q
            node.next = p
            q.next = node
            p.prev = node
        else:
            node.prev = q
            q.next = node

    return head


n = int(input())
link = DoublyLinkedList()
for _ in range(n):
    link.insert(int(input()))
target = int(input())
link.head = sorted_insert(link.head, target)
display(link.head)