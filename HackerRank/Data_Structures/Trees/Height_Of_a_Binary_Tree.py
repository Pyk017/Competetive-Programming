class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if not root:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        return root

def preorder_traversal(root):
    if root:
        print(root.data)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def height(root):
    return -1 if not root else max(1 + height(root.left), 1 + height(root.right))

tree = Tree()
inp = list(map(int, input().split()))
for i in inp:
    tree.root = tree.insert(tree.root, i)
# preorder_traversal(tree.root)
print(height(tree.root))