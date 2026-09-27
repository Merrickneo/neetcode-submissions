# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checker(root):
            if not root:
                return True
            self.isBalanced(root.left)
            self.isBalanced(root.right)
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            if abs(left_height - right_height) > 1:
                self.balanced = False 
            return abs(left_height - right_height) <= 1 
        checker(root)
        return self.balanced
        
    
    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left) + 1
        right = self.height(root.right) + 1
        return max(left, right)
    

        