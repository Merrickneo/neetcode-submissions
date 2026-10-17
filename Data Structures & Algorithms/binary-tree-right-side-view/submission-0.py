# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
'''
Iteration pattern seems like we have to do BFS.
Right side view need not necessarily mean the right most value
- Defn should be the rightmost element in the level
- Should be the same iteration pattern as levelOrder traversal
- Process each row, check the size of the current level then get the right most one
'''


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = []
        queue = deque(list())
        queue.append(root)
        while queue:
            i = 1
            n = len(queue)
            while i <= n:
                node = queue.popleft()
                if i == n:
                    output.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i += 1
        return output
                    



        