from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level = []
            n = len(queue)

            # Length of queue wont be re-calculated inside the for loop, allows to process each level
            for _ in range(n):
                curr = queue.popleft() # FIFO
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            # Get the result of the specific level above
            res.append(level)

        return res
