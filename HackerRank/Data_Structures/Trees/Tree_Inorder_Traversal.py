class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)

        else:
            node = Node(data)
            p = self.root
            q = None
            while p:
                q = p
                if p.data > data:
                    p = p.left
                else:
                    p = p.right
            
            if q.data < data:
                q.right = node
            else:
                q.left = node
            node.parent = q


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)


tree = Tree()
arr = list(map(int, input().split()))
for i in arr:
    tree.insert(i)
inOrder(tree.root)
