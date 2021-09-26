import sys
from collections import deque
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

def cal_heightBST(root):
    if (root is None ):
        return 0
   
    return 1 + max(cal_heightBST(root.left), cal_heightBST(root.right))
a = deque()
n = 0
while (True):
    b = list(map(int,sys.stdin.readline().split()))
    if (b[0] == 0):
        a.insert(0,b[1])
    elif (b[0] == 1):
        a.append(b[1])
    elif (b[0] == 2):
        try:
            a.insert(a.index(b[1]) + 1, b[2])
        except:
            a.insert(0, b[2])
    elif (b[0] == 3 ):
        break
    n += 1



root = None
for i in a:
    root = insert(root,i)

print(cal_heightBST(root))