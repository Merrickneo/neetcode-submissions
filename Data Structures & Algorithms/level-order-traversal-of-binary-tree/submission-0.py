# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
BFS to append elements to the list whereby we do it per level
1. When we do the level order we return
'''

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        output = []
        while queue:
            i = 0
            n = len(queue)
            level_output = []
            while i < n:
                node = queue.pop(0)
                level_output.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i += 1
            output.append(level_output)
        return output


        
        