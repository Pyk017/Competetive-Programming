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



def top_view(root):
    if not root:
        return 
    q = []
    m = dict()
    hd = 0
    root.hd = hd
    q.append(root)
    while len(q):
        root = q[0]
        hd = root.hd
        if hd not in m:
            m[hd] = root.data
        if root.left:
            root.left.hd = hd - 1
            q.append(root.left)
        if root.right:
            root.right.hd = hd + 1
            q.append(root.right)
        
        q.pop(0)
    
    for i in sorted(m):
        print(m[i], end=' ')


tree = Tree()
arr = list(map(int, input().split()))
for i in arr:
    tree.insert(i)
# inOrder(tree.root)
top_view(tree.root)