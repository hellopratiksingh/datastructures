# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder and not inorder:
            return None

        root = TreeNode(preorder[0])
        # mid tells us partition how much left and how much right
        # Inorder sequence: D B E mid F C (3 left 2 right) thats why 
        # preorder[mid] in left (due to python its preorder[1:mid+1) and preorder[mid+1:] in right
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root


# Inorder sequence: D B E A F C
# Preorder sequence: A B D E C F
