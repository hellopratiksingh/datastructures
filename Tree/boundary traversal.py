'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


class Solution:
    def traverseleft(self, root, res):
        if (root == None) or (not root.left and not root.right):
            return

        res.append(root.data)
        if root.left:
            self.traverseleft(root.left, res)
        else:
            self.traverseleft(root.right, res)

    def traverseleaf(self, root, res):
        if root == None:
            return

        if not root.left and not root.right:
            res.append(root.data)
            return

        self.traverseleaf(root.left, res)
        self.traverseleaf(root.right, res)

    def traverseright(self, root, res):
        if (root == None) or (not root.left and not root.right):
            return
        if root.right:
            self.traverseright(root.right, res)
        else:
            self.traverseright(root.left, res)
        res.append(root.data)

    def printBoundaryView(self, root):
        if root == None:
            return

        res = []
        res.append(root.data)

        self.traverseleft(root.left, res)

        self.traverseleaf(root.left, res)
        self.traverseleaf(root.right, res)

        self.traverseright(root.right, res)
        return res
