class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

    def __init__(self):
        return str(self.info)

class Tree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=' ')


tree = Tree()
arr = list(map(int, input().split()))
for i in arr:
    tree.create(i)
postOrder(tree.root)
