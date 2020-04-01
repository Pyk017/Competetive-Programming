class Node:
    def __init__(self, data):
        self.data = data
<<<<<<< HEAD
        self.right = None
        self.left = None
=======
        self.left = None
        self.right = None
>>>>>>> 70e0272bed1af72b44ea7e54427038b1bfe8271b
        self.parent = None

class Tree:
    def __init__(self):
        self.root = None
<<<<<<< HEAD

    def insert(self, root, data):
        if not root:
            return Node(data)

=======
    
    def insert(self, root, data):
        if not root:
            return Node(data)
        
>>>>>>> 70e0272bed1af72b44ea7e54427038b1bfe8271b
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

<<<<<<< HEAD

=======
>>>>>>> 70e0272bed1af72b44ea7e54427038b1bfe8271b
tree = Tree()
inp = list(map(int, input().split()))
for i in inp:
    tree.root = tree.insert(tree.root, i)
preorder_traversal(tree.root)
