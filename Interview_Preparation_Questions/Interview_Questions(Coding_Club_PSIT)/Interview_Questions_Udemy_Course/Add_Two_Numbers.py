# We are given a two empty Linked List, and the two linked list representing two integers, 
# the digits are stored in reversed order and every Node
# contains single digit. Add the two numbers and return it as a linked list. 
# Example : Number 1: 2 -> 4 -> 3 = 342
#           Number 2: 5 -> 6 -> 4 = 465   (After addition answer is 807)
# Output :   7 -> 0 -> 8

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
        return self.head


def display(head):
    p = head
    while p:
        print(p.data, end=' ')
        p = p.next

def add(head1, head2, list4):
    temp = 0
    while head1 and head2:
        a = head1.data + head2.data + temp
        if len(str(a)) == 2:
            temp = int(str(a)[0])
            list4.head = list4.insert(int(str(a)[1]))
        else:
            list4.head = list4.insert(a)
        head1 = head1.next
        head2 = head2.next

    while head1:
        list4.head = list4.insert(head1.data + temp)
        head1 = head1.next

    while head2:
        list4.head = list4.insert(head2.data + temp)
        head2 = head2.next


num1 = list(input())
num2 = list(input())
list1 = LinkedList()
list2 = LinkedList()
list3 = LinkedList()
for i, j in zip(num1[::-1], num2[::-1]):
    list1.head = list1.insert(int(i))
    list2.head = list2.insert(int(j))

# display(list1.head)
# display(list2.head)
add(list1.head, list2.head, list3)
display(list3.head)
