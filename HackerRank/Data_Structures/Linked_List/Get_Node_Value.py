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


def get_node_value(head, pos):
    total = 0
    p = head
    while p:
        p = p.next
        total += 1
    p = head
    m = total - pos - 1
    for _ in range(m):
        p = p.next

    return p.data


n = int(input())
link = LinkedList()
for _ in range(n):
    link.insert(int(input()))
pos = int(input())
res = get_node_value(link.head, pos)
print(res)
