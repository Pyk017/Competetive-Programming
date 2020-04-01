class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None


def insert(root,data):
    if root is None :
        return Node(data)

    if data < root.data :
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


def printLevelOrder(root):
    if root is None:
        return None
    else:
        q = []
        q.append(root)
        while len(q) > 0:
            print (q[0].data, end=" ")
            node = q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)


def height(root):
    return -1 if root is None else max(1 + height(root.left), 1 + height(root.right))


tree = Tree()
arr = list(map(int, input().split()))
for i in arr:
    tree.root = insert(tree.root, i)
printLevelOrder(tree.root)
