# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output = []
        queue = deque(list())
        queue.append(root)
        while queue:
            i = 0
            n = len(queue)
            level_elems = []
            while i < n:
                node = queue.popleft()
                level_elems.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i += 1
            output.append(level_elems)
        return output
        