class Node:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value
def insert(root,value):
    if (root is None):
        root = Node(value)
        return root
    if (root.value < value):
        root.right = insert(root.right,value)
    elif (root.value > value):
        root.left = insert(root.left,value)
    return root


def printBFS(root):
    q = []
    d = 0
    c = 0
    q.append(root)
    c = c + 1
    while (d < c):
        x = q[d]
        d = d + 1
        print(x.value,end = ' ')
        if (x.left is not None):
            c = c + 1
            q.append(x.left)
        if (x.right is not None):
            c = c + 1
            q.append(x.right)

    return 

root = None
while (True):
    x = int(input())
    if (x == 0):
        printBFS(root)
        break
    else:
        root = insert(root , x)

    