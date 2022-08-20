from collections import deque

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def changeToDepthTree(root):
    if root == None:
        return
    q = deque()
    p = root
    p.data = 0
    q.append(p)
    while q:
        p = q.popleft()
        if p.left:
            p.left.data = p.data + 1
            q.append(p.left)

        if p.right:
            p.right.data = p.data + 1
            q.append(p.right)
