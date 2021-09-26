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


def Count_Node_la(root):
    if (root is None):
        return 0
    if (root.left is None and root.right is None):
        return 1
    return Count_Node_la(root.left)+Count_Node_la(root.right)



root = None
while (True):
    x = int(input())
    if (x == 0):
        print(Count_Node_la(root))
        break
    else:
        root = insert(root , x)

    