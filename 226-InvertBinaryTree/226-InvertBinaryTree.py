# Last updated: 23/07/2026, 10:59:24
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root):
        if not root:
            return None
        
        # Swap children
        root.left, root.right = root.right, root.left
        
        # Recurse
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root