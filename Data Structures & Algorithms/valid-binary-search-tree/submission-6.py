# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True
        def traversal(node, low, high):
            nonlocal valid
            if not node:
                return
            if not (low < node.val < high):
                valid = False
            traversal(node.left, low, node.val)
            traversal(node.right, node.val, high)
        traversal(root, -float('inf'), float('inf'))
        return valid

