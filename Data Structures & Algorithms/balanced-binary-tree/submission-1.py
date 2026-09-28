# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
1. Need to check each node if its balanced
2. Check by each node's left and right height are less than 1 in
terms of the difference
'''
class Solution:
    balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def checker(root):
            if not root:
                return True
            self.isBalanced(root.left)
            self.isBalanced(root.right)
            left = self.height(root.left)
            right = self.height(root.right)
            if abs(left - right) > 1:
                self.balanced = False
        checker(root)
        return self.balanced
    
    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return max(left, right) + 1
        